import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from math import factorial

n = 10
a_0 = 5.29177210903e-11

X = np.linspace(-1e-10, 1e-10, n)
Y = X
Z = X


points = []
for x in X:
    for y in Y:
        for z in Z:
            print(x, y, z)
            print(toPol(x, y, z))
            print()
            points.append(toPol(x, y, z))
points = np.array(points)


def L(alpha, k, x):
    pass

def P(m, l, x):
    pass


def PR(r, n, l):
    return np.sqrt((2/(n * a_0))**3 * factorial(n - l + 1) / (2 * n * factorial(n + l))) * np.exp(-r/(n * a_0)) * (2 * r / (n * a_0))**l * L(2*l+1, n-l-1, 2*r/(n * a_0))

def PY(l, m, theta, phi):
    return np.sqrt(((2 * l + 1)*factorial(l - m))/(4 * np.pi * factorial(l + m))) * P(m, l, np.cos(theta)) * np.exp(m * phi * complex(0, 1))


def Psi(r, theta, phi, m, l, s):
    pass


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

points = np.transpose(points)

xs, ys, zs = np.meshgrid(X, Y, Z)

ax.scatter(xs, ys, zs)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()