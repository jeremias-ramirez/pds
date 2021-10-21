import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-20, 21, 0.05)
fc1 = 2 * (x+1)**2 + 5
fc2 = 2 * (x-3)**2 + 1

fc3 = 2 * (x)**2 

fsum = fc1 + fc2 + fc3 
idxMin = np.argmin(fsum)

plt.xlim(-5, 5)
plt.ylim(0, 55)

plt.plot(x, fc1,"r.", x, fc2, "b.", x, fc3, x, fsum, "g.")
plt.plot(x[idxMin], fsum[idxMin], "k*")
plt.vlines(x = x[idxMin], ymin = 0, ymax = fsum[idxMin], color="k")
plt.show()


