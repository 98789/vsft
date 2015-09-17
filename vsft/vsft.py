from numpy import abs
from numpy import arange
from numpy import asarray
from numpy import dot
from numpy import exp
from numpy import log2
from numpy import pi
from numpy import vstack
from numpy import zeros

def exponential(nk, N):
   """exponential weight"""

   return exp(-2j * pi * nk / N)

def triangular(nk, N):
   """triangular weight"""

   nk %= N
   W = 2 * abs( 2 * nk / N - 1) - 1 + 0j
   W[nk < N/2] += (1 - abs(4 * nk / N - 1))[nk < N/2] * 1j
   W[nk >= N/2] += (abs(4 * nk / N - 3) - 1)[nk >= N/2] * 1j

   return W

def fft(x, N=1024, W=exponential, rec_index=32):
    """perform fft"""

    N = min(N, x.shape[0])
    N = 2**int(log2(N))
    rec_index = 2**int(log2(rec_index))

    x = asarray(x[:N], dtype=complex)

    N_min = min(N, rec_index)
    
    n = arange(N_min)
    k = n[:, None]
    M = W(n*k, N_min)
    X = dot(M, x.reshape((N_min, -1)))

    while X.shape[0] < N:
        X_even = X[:, :X.shape[1] / 2]
        X_odd = X[:, X.shape[1] / 2:]
        factor = W(arange(X.shape[0]), X.shape[0]*2)[:, None]
        X = vstack([X_even + factor * X_odd,
                       X_even - factor * X_odd])

    return X.ravel()
