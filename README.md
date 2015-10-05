# vsft

Vectorized implementation of FFT algorithm which allows the use of custom weights.
This implementation relies on a modified and parameterized version of the Vanderplas'
code located at https://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/

fft(x, N=0, W=exponential, rec_index=32)

Inputs:

x: vector of samples (time domain).  
N: Number of outputs.  
W: Weight to be used: exponential, triangular or any user defined weight function.  
rec_index: Cutoff, an initial vectorized DFT is performed with the first rec_index
           samples. If the size of x is lower than rec_index a vectorized DFT takes
           place.  

Outputs:

Vector X of size N (frequency domain).
