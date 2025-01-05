
import numpy as np
import matplotlib.pyplot as plt
import random as rd
from coord_translation import topol, tocart
from functions import Mintegral, SMintegral
from probability import boolout

L = 10

N = 10 * L

def f(x):
    return 1/(x+1)**2

mesh = np.linspace(0, L, N)

fspace = f(mesh)

abs = fspace / sum(fspace)

barlist = [0 for i in mesh]

for j in range(2000):
    for i, e in enumerate(abs):
        test = boolout(e)
        if test == True:
            barlist[i] += 1

m = max(barlist)

barlist = np.array(barlist) / m * max(abs)

err = np.sqrt((barlist-abs)**2)

plt.plot(mesh, abs)
plt.plot(mesh, barlist)
plt.show()
plt.plot(mesh, err)
plt.show()