from operator import concat
import numpy as np
from scipy import signal
from akaike import akaike
from autocorrelacion import autocorrelacion
from levinson_durbin import levison_durbin as levin
from matplotlib import pyplot as plt
from scipy.signal import freqz
from scipy.fft import fft, ifft, fftfreq
import math

reader = open("eeg.txt", "r")
eeg = np.array( [np.double(line.strip()) for line in reader.readlines()] )
eeg = eeg/max(abs(eeg))

p = 60 
r = autocorrelacion(eeg, p)
(A, E) = levin(r, p)
N = eeg.size
[I, iMin] = akaike(E, N)

b = [1]
a = np.concatenate(([1], A[:, iMin-1]))
w, h = freqz(b, a) 
fm = 250

SAMPLE_RATE = 1 / N
yf = fft(eeg)
xf = fftfreq(N)
M = N// 2
print(xf[:M+1])
plt.plot(xf[:M] , np.abs(yf[:M]))
plt.plot(w, np.abs(h))
plt.show()