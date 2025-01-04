
import numpy as np

def integral(f, x, y, N):
    m = np.linspace(x, y, N)
    dx = (y-x)/N
    return f(m + dx/2) * dx

def Mintegral(f, mesh):
    dx = (mesh[-1]-mesh[0])/len(mesh)
    return f(mesh  + dx/2) * dx

def SMintegral(f, mesh):
    dx = (mesh[-1]-mesh[0])/len(mesh)
    return sum(f(mesh + dx/2) * dx)