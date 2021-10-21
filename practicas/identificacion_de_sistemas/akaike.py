import numpy as np
def akaike(E, N):
    I = np.log2(E[1:]) + 2*np.arange(1, E.size) / N
    return (I, np.argmin(I) + 1)