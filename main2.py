import numpy as np
from numpy.polynomial import Polynomial
import matplotlib.pyplot as plt
import scipy as sp
from math import factorial, comb
from coord_translation import *
from functions import *

n = 10
a_0 = 5.29177210903e-11
a_0 = 1 

X = np.linspace(-1e-10, 1e-10, n)
Y = X
Z = X

points = []
for x in X:
    for y in Y:
        for z in Z:
            points.append(toPol(x, y, z))
points = np.array(points)


def L(a, k, x):
    return sum([(-1)**i * comb(k+a, k-i) * x**i / factorial(i) for i in range(k+1)])

def P(m, l, x):
    pol = Polynomial([-1, 0, 1])
    if l == 0:
        pol = 1
    else:
        for i in range(l+1):
            pol = pol * pol

        for i in range(m + l):
            pol = pol.deriv()

    return (-1)**m * (1-x**2)**(m/2) * 1/(2**l * factorial(l)) * pol(x)


def R(r, n, l):
    return np.sqrt((2/(n * a_0))**3 * factorial(n - l - 1) / (2 * n * factorial(n + l))) * np.exp(-r / (n * a_0)) * (2 * r / (n * a_0))**l * L(2*l + 1, n-l-1, 2 * r/(n * a_0))


def PY(l, m, theta, phi):
    return np.sqrt(((2 * l + 1)*factorial(l - m))/(4 * np.pi * factorial(l + m))) * P(m, l, np.cos(theta)) #* np.exp(m * phi * complex(0, 1))

x = np.linspace(0, 20*a_0, 1000)
theta = np.linspace(0, np.pi, 1000)
phi = np.linspace(0, 2*np.pi, 1000)
print("R: Simpson's method predicts: ", sp.integrate.simpson(R(x, 2, 1)**2 * x**2, x))
print()
print("Y: Simpson's method predicts: ", sp.integrate.simpson(PY(1, 0, theta, phi) * PY(1, 0, theta, phi)) * 2*np.pi)

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