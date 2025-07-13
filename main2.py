import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
import scipy as sp
from coord_translation import *
from functions import *
import random as rp
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

%matplotlib widget

n   = 75
a_0 = 5.29177210903e-11
a_0 = 1

X = np.linspace(-15*a_0, 15*a_0, n)
Y = X
Z = X

xs, ys, zs = np.meshgrid(X, Y, Z)

n = 2
l = 1
m = 0


points = []
for i in range(2):
    for x in X:
        for y in Y:
            for z in Z:
                if x >= 0 and y <= 0:
                    None
                else:
                    if PsiCart(x, y, z, m, l, n) > rp.uniform(0, 1):
                        points.append(np.array([x, y, z]))
points = np.array(points)
points = np.transpose(points)



xp = points[0]
yp = points[1]
zp = points[2]

Xs, Ys, Zs = np.meshgrid(xp, yp, zp)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')


ax.scatter(xp, yp, zp)

ax.scatter(0, 0, 0, color="red")

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()