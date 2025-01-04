import numpy as np
import random as rp

def boolout(P):
    p = str("0.")
    for i in range(len(str(P)) - 2):
        p += str(rp.randint(0, 9))
    print(p)
    p = float(p)
    if p <= P:
        return True
    elif p > P:
        return False

def placefunc(mesh, f):
    