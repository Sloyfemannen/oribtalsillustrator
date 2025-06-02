import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
import scipy as sp
from math import factorial, comb
from coord_translation import *
from functions import *
from probability import boolout

n = 10
a_0 = 5.29177210903e-11
a_0 = 1

X = np.linspace(-10*a_0, 10*a_0, n)
Y = X
Z = X


fig = plt.figure()
ax = fig.add_subplot(projection='3d')


xs, ys, zs = np.meshgrid(X, Y, Z)

px, py, pz = 

ax.scatter(xs, ys, zs)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()