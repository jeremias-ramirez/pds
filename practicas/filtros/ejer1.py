import math
import numpy as np
from numpy.lib.polynomial import poly
import matplotlib.pyplot as plt
from zplane import zplane

#definir polos y cero
r1 = 0.95
r2 = 0.80
toRadians = lambda g: g * math.pi / 180
a1 = toRadians(45)
a2 = toRadians(30)
a3 = toRadians(60) 

toPolar = lambda r, ang : r * np.exp(1j * ang)
p = [toPolar(r1, a1), toPolar(r1, -a1), toPolar(r1, a1), toPolar(r1, -a1)]
c = [toPolar(r1, a2), toPolar(r1, -a2), toPolar(r2, a3), toPolar(r2, -a3)]

#polinomios
num = np.poly(c)
den = poly(p)

#zplane(num, den)

#respuesta en frecuencia

np.z


