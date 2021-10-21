from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

N = 900050;

cuadrada = np.ones(N);
hamming = signal.windows.hamming(N);

energia = lambda arr: np.dot(arr, arr)
relacion_energia = energia(hamming) / energia(cuadrada)
plt.plot(np.arange(N), hamming)
plt.show()
print(relacion_energia)
