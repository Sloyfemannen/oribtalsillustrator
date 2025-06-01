
import numpy as np
import regex as rg

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