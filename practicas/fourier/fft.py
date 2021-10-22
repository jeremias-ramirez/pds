#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 16:21:53 2021

@author: jeremias
"""

from scipy.fft import fft, ifft, fftfreq
from scipy.signal import convolve, correlate
from numpy.linalg import norm
import numpy as np
import señales.generate_sine_wave as gs
from matplotlib import pyplot as plt

#propiedad de convolucicón
x = [1, 2, 2]
h = [2, 1, 0.5]

N = len(x)

conv = convolve(x, h)

result = ifft(fft(x) * fft(h))

x_m = x + [0]*(len(x) - 1 )
h_m = h + [0]*(len(h) - 1)

x_m_fourier = fft(x_m)
h_m_fourier = fft(h_m)

product_m = x_m_fourier * h_m_fourier

result_m = ifft(product_m)

#señal para verificar las propiedades

SAMPLE_RATE = 100
DURATION = 1
N = SAMPLE_RATE * DURATION

x, y_sin5  = gs.generate_sine_wave(5, SAMPLE_RATE, DURATION)
_, y_sin8  = gs.generate_sine_wave(8, SAMPLE_RATE, DURATION)

y = y_sin5 + 2 * y_sin8


yf = fft(y)
xf = fftfreq(N, 1/SAMPLE_RATE)

#plt.scatter(xf, np.abs(yf))

#propiedad de simetria

yf_f = fft(yf/len(x))
yf_if_iy = ifft(yf)[::-1]


plt.plot(x, yf_f, x, yf_if_iy)

#propiedad de modulacion

y_exp_i3 = y * np.exp(1j*2*np.pi*(1/N)*np.arange(N)*3)

y_exp_i3f = fft(y_exp_i3)

f1 = plt.figure()
a1 = f1.add_axes([0, 0, 1, 1])

a1.scatter(xf, np.abs(yf))
a1.scatter(xf, np.abs(y_exp_i3f))
a1.set_xlim(-20, 20)

#Teorema de Parseval
norm_y  = norm(y, 2)**2 
norm_yf = norm(yf, 2)**2 / N

#propiedad de correlación
    
corr = correlate(y_sin5, y_sin8, mode= "full", method="direct")

yf_sin5 = fft(np.concatenate((y_sin5, np.zeros(N-1))))
yf_sin8 = fft(np.concatenate((y_sin8, np.zeros(N-1))))

product_sin5_conj_sin8 = yf_sin5 * np.conjugate(yf_sin8)
result_product = ifft(product_sin5_conj_sin8)

f2 = plt.figure()
a2 = f2.add_axes([0, 0, 1, 1])
a2.plot(np.arange(2*N - 1), corr)
a2.plot(np.arange(2*N - 1), result_product)

