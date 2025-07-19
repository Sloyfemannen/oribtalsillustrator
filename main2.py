import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
import scipy as sp
from functions import *
import random as rp
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

%matplotlib widget

a_0 = 5.29177210903e-11
a_0 = 1

X = np.linspace(-15*a_0, 15*a_0, 75)
Y = X
Z = X

n = 2
l = 1
m = 0


points = []
for i in range(2):
    for x in X:
        for y in Y:
            for z in Z:
                if x > 0 and y > 0:
                    None
                else:
                    P = PsiCart(x, y, z, m, l, n)
                    if P > rp.uniform(0, 1):
                        c = P * 50
                        points.append(np.array([x, y, z, c]))
points = np.array(points)
points = np.transpose(points)



xp = points[0]
yp = points[1]
zp = points[2]
cr = points[3]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')


ax.scatter(xp, yp, zp, c=cr, cmap='viridis', alpha=1)

ax.scatter(0, 0, 0, color="red")

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

ax.view_init(elev=10, azim=45, roll=0)
plt.show()