import numpy as np
from scipy import signal
from akaike import akaike
from autocorrelacion import autocorrelacion
from epf import epf
from levinson_durbin import levison_durbin as levin
from matplotlib import pyplot as plt

x = np.random.random(1000)
x = x - np.mean(x)

b = [1]
a = [1, -0.3, 0.4, -0.2]
y = signal.lfilter(b, a, x).flatten()
p = 10
r = autocorrelacion(y, p)
[A, E] = levin(r, p)
(epfV, p1) = epf(E, r[0], 0.01)
(akaikeV, p2) = akaike(E, y.size)

pV = np.arange(1, p + 1)
sub1 = plt.subplot(1,2, 1)
sub1.plot(pV, epfV, "r")

sub2= plt.subplot(1,2, 2)
sub2.plot(pV, akaikeV, "b")
#plt.show()
print(E[p2])