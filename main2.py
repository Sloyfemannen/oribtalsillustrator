import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
import scipy as sp
from math import factorial, comb
from coord_translation import *
from functions import *
from probability import boolout
import random as rp
from mpl_toolkits.mplot3d import Axes3D

%matplotlib widget

np.random.seed(19680801)

n = 40
a_0 = 5.29177210903e-11
a_0 = 1

X = np.linspace(-5*a_0, 5*a_0, n)
Y = X
Z = X

xs, ys, zs = np.meshgrid(X, Y, Z)

n = 1
l = 0
m = 0

counter = 0

points = []
for i in range(1):
    for x in X:
        for y in Y:
            for z in Z:
                if PsiCart(x, y, z, m, l, n) > rp.uniform(0, 1):
                    points.append(np.array([x, y, z]))
                if PsiCart(x, y, z, m, l, n) < 1:
                    counter += 1
points = np.array(points)
points = np.transpose(points)

xp = points[0]
yp = points[1]
zp = points[2]

Xs, Ys, Zs = np.meshgrid(xp, yp, zp)

fig = plt.figure()
#ax = fig.add_subplot(projection='3d')
ax = Axes3D(fig)


plot_geeks = ax.scatter(xp, yp, zp)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

print(counter)