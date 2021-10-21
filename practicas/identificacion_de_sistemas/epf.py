def epf(E, r0, gamma):
    V = E/r0
    est = 1 - V[1:] / V[:-1] 
    p = sum([ est[idx] > gamma for idx in range(E.size - 1) ]) + 1
    return (est, p)