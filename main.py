
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

xmesh = np.linspace(L/N, L, N)

xmesh, ymesh = np.meshgrid(np.linspace(L/N, L, N), np.linspace(L/N, L, N))

fspace = f(xmesh)

plt.plot(xmesh, fspace)
plt.show()

abs = fspace / sum(fspace)

barlist = [0 for i in xmesh]

for j in range(1000):
    for i, e in enumerate(abs):
        test = boolout(e)
        if test == True:
            barlist[i] += 1
            plt.plot(xmesh[i], rd.uniform(0, 1), 'ro')

plt.show()

m = max(barlist)

barlist = np.array(barlist) / m * max(abs)

sqerr = (barlist-abs)**2

plt.plot(xmesh, abs)
plt.plot(xmesh, barlist)
plt.show()
plt.plot(xmesh, sqerr)
plt.show()