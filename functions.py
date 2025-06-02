
import numpy as np
from numpy.polynomial import Polynomial
from math import comb, factorial, sqrt
import regex as rg
import scipy as sp
from scipy.special import lpmv
from scipy.integrate import simpson
import matplotlib.pyplot as plt

def integral(f, x, y, N):
    m = np.linspace(x, y, N)
    dx = (y-x)/N
    return f(m + dx/2) * dx

def Mintegral(f, mesh):
    dx = (mesh[-1]-mesh[0])/len(mesh)
    return f(mesh  + dx/2) * dx

def SMintegral(f, mesh):
    return sum(Mintegral(f, mesh))

def floatint(n):
    N = str(n)
    N = rg.sub('[.]', '', N)
    return int(N)

def randfloat(a, b):
    return None


########################

a_0 = 1

def L(a, k, x):
    return sum([(-1)**i * comb(k+a, k-i) * x**i / factorial(i) for i in range(k+1)])

def P(l, m, x=0):
    pol = Polynomial([-1, 0, 1])
    pol = pol ** l

    for i in range(m + l):
        pol = pol.deriv()
    
    return (-1)**m * (1-x**2)**(m/2) * 1/(2**l * factorial(l)) * pol(x)


def R(r, n, l):
    return np.sqrt((2/(n * a_0))**3 * factorial(n - l - 1) / (2 * n * factorial(n + l))) * np.exp(-r / (n * a_0)) * (2 * r / (n * a_0))**l * L(2*l + 1, n-l-1, 2 * r/(n * a_0))

def PY(l, m, theta, phi):
    norm = sqrt((2 * l + 1) * factorial(l - m) / (4 * np.pi * factorial(l + m)))
    ex = np.exp(m * phi * 1j)
    P = lpmv(m, l, np.cos(theta))
    return norm * P * ex

def Psi(r, theta, phi, m, l, s):
    return r**2 * abs(R(r, s, l))**2 * abs(PY(l, m, theta, phi))**2