import numpy as np

def levison_durbin(r, p):
    A = np.zeros((p, p))
    E = np.zeros(p+1)
    k = np.zeros(p)
    E[0]= r[0]

    get_k = lambda i : -1/E[i] * (r[i+1] + np.dot(A[0:i, i-1] , r[i:0:-1]))

    for i in range(p):
        k = get_k(i)
        A[i, i] = k
        if i > 0: 
            A[0:i, i] = np.array([A[j,i-1] + k * A[i-1-j, i-1] for j in range(i)])
        E[i+1] = E[i] * (1 - k**2)
    
    return A, E
