
from numpy import cos, sin, acos, asin, atan

def tocart(r, deg):
    x = r * cos(deg)
    y = r * sin(deg)
    return [x, y]

def torot(x, y):
    r = x**2 + y**2
    deg = atan(y/x)
    return [r, deg]