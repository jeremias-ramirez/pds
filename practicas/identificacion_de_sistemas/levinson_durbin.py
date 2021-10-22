import numpy as np
def levison_durbin(r, p):

    '''
    Algoritmo de Levison-Durbin para la obtención de los coeficientes a de la ecuación
    r=Ra
    
    Parameters
    ----------
    r : numpy array
        vector de correlación, con un tamaño de p+1
    p : int 
        numero de coeficientes a_i que se quieren obtener
    
    Returns
    -------
    A: numpy matrix
        matriz con los coeficiente a_i de cada iteración, están ordenado por 
        columnas, cada columna i tiene los coeficientes del orden i + 1
    E: numpy array
        error cuadratico medio total obtenido por las iterracción
        de tamaño p + 1 E[0] es la autocorrelación sin desplazamiento (Energía)
    '''
    



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
