
import numpy as np
import matplotlib.pyplot as plt
import random as rd
from coord_translation import topol, tocart
from functions import Mintegral, SMintegral

L = 10

N = 100 * L

def f(x):
    return 1/(x+1)**2

mesh = np.linspace(0, L, N)

fspace = f(mesh)

integ = fspace / sum(fspace)

abs = fspace * integ

#abs = abs / abs[0]

plt.plot(mesh, abs)
#plt.plot(mesh, fspace)
plt.show()

