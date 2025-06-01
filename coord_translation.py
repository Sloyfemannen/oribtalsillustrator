
from numpy import cos, sin, arccos, arcsin, arctan, sqrt, array

def tocart(r, deg):
    x = r * cos(deg)
    y = r * sin(deg)
    return [x, y]

def topol(x, y, z=0):
    r = x**2 + y**2
    deg = arctan(y/x)
    return array[r, deg]

def toCart():
    pass

def toPol(x, y, z):
    r     = sqrt(x**2 + y**2 + z**2)
    theta = arccos(z / r)
    phi   = arctan(y / x)
    return array([r, theta, phi])