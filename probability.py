import numpy as np
import random as rp

def boolout(P):
    p = rp.uniform(0, 1)
    if p <= P:
        return True
    elif p > P:
        return False

def fstring(mesh, f):
    fmesh = {}
    for i in mesh:
        if len(fmesh) == 0:
            fmesh.update({i: f(i)})
        else:
            fmesh.update({i, f(i) + fmesh[-1]})
    return fmesh