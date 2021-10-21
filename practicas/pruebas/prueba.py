#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 17:34:57 2021

@author: jeremias
"""

import generate_sine_wave as gsw
from scipy.fft import fft, fftfreq
from generate_sine_wave import generate_sine_wave
from matplotlib import pyplot as plt
import numpy as np

_, y = gsw.generate_sine_wave(1, 4, 1)

x, y4 = gsw.generate_sine_wave(4, 100, 1)

plt.plot(x, y4)
plt.show()
yf = fft(y)

xf = fftfreq(4, 1/4)

#plt.scatter(xf, np.abs(yf))
