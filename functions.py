
import numpy as np
from numpy.polynomial import Polynomial
from math import comb, factorial, sqrt
import regex as rg
from scipy.special import lpmv
from scipy.integrate import simpson
from math import cos, sin, acos, asin, atan, pi
import random as rd


def tocart(arr):
    r     = arr[0]
    theta = arr[1]
    phi   = arr[2]
    x = r * sin(theta) * cos(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(theta)
    return [x, y, z]

def topol(arr):
    x = arr[0]
    y = arr[1]
    z = arr[2]
    r     = sqrt(x**2 + y**2 + z**2)
    theta = acos(z / r)
    phi   = atan(y / x)
    if x < 0:
        phi += pi
    return [r, theta, phi]


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

def boolout(P):
    p = rd.uniform(0, 1)
    if p <= P:
        return True
    elif p > P:
        return False

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

def PsiSphr(r, theta, phi, m, l, n):
    return r**2 * abs(R(r, n, l))**2 * abs(PY(l, m, theta, phi))**2

def PsiCart(x, y, z, m, l, n):
    pol = topol([x, y, z])
    r = pol[0]
    theta = pol[1]
    phi = pol[2]
    ProbDens = PsiSphr(r, theta, phi, m, l, n)
    return ProbDens

def StochasticPoint(x, y, z, m, l, n):
    dice = boolout(PsiCart(x, y, z, m, l, n))
    if dice == True:
        return np.array(x, y ,z)

def bound(n, l):
    integral = 0
    a = 0
    while integral < 0.999:
        a += 1
        r = np.linspace(0, a, 1000)
        P = R(r, n, l)
        integral = simpson(P**2 * r**2, r)
    return a