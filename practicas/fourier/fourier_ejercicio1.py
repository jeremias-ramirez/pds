#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 17:17:31 2021

@author: jeremias
"""


from scipy.fft import fft, fftfreq
from generate_sine_wave import generate_sine_wave
from matplotlib import pyplot as plt
import numpy as np


DT = 0.004 #seconds
SAMPLE_RATE = int(1/DT)  # Hertz
DURATION = 1  # Seconds


f1 = 10
_, y1 = generate_sine_wave(f1, SAMPLE_RATE, DURATION)

f2 = 11
_, y2 = generate_sine_wave(f2, SAMPLE_RATE, DURATION)

y = y1 + 4 * y2 +4

yf= fft(y)

N = SAMPLE_RATE * DURATION

xf = fftfreq(N, 1 / SAMPLE_RATE)

plt.scatter(xf, np.abs(yf))
"""
y2s = np.concatenate((y1 + 4 * y2, [0]  * (N - len(y1))))

y2f= fft(y2s)

#plt.scatter(xf, np.abs(y2f))

"""












