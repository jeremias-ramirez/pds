import numpy as np

def autocorrelacion(x, N): 
    #acorr_full = np.correlate(x, x, "full");
    #return acorr_full[acorr_full.size //2 : N + acorr_full.size //2 ] /x.size
    return np.array([np.dot(x[p:], x[:x.size - p]) for p in range(N+1)]) / x.size

#x= np.array([1, 2, 3])
#print(autocorrelacion(x, 3))