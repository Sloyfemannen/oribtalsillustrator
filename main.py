
import numpy as np
import matplotlib.pyplot as plt
import random as rd
from coord_translation import topol, tocart
from functions import Mintegral, SMintegral
from probability import boolout

L = 20

N = 100 * L

def f(x):
    return np.sin(x)**2 /x

mesh = np.linspace(L/N, L, N)

fspace = f(mesh)

plt.plot(mesh, fspace)
plt.show()

abs = fspace / sum(fspace)

barlist = [0 for i in mesh]

for j in range(1000):
    for i, e in enumerate(abs):
        test = boolout(e)
        if test == True:
            barlist[i] += 1
            plt.plot(mesh[i], rd.uniform(0, 1), 'ro')

plt.show()

m = max(barlist)

barlist = np.array(barlist) / m * max(abs)

sqerr = (barlist-abs)**2

plt.plot(mesh, abs)
plt.plot(mesh, barlist)
plt.show()
plt.plot(mesh, sqerr)
plt.show()