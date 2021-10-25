import numpy as np
from akaike import akaike
from autocorrelacion import autocorrelacion
from levinson_durbin import levison_durbin as levin
from matplotlib import pyplot as plt
from scipy.signal import freqz
from scipy.fft import fft,  fftfreq
import math

reader = open("eeg.txt", "r")
eeg = np.array( [np.double(line.strip()) for line in reader.readlines()] )
eeg = eeg/max(abs(eeg))

p = 60 
r = autocorrelacion(eeg, p)
(A, E) = levin(r, p)
N = eeg.size
[I, iMin] = akaike(E, N)
print(iMin)
b = [1]
a = np.concatenate(([1], A[:, iMin-1]))
w, h = freqz(b, a) # w va de 0 a pi

fm = 250
w = (w * fm) / (2 * np.pi) # la escalo de  0 a fm/2

SAMPLE_RATE = 1 / N
yf = fft(eeg)
N = len(yf)
M = N // 2 + 1  # 
xf = fm/N  * np.arange(M, step=1) 

plt.plot(xf , np.abs(yf[:M]))
plt.plot(w, np.abs(h))
plt.show()