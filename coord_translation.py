
from numpy import cos, sin, arccos, arcsin, arctan, sqrt, pi

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
    theta = arccos(z / r)
    phi   = arctan(y / x)
    if x < 0:
        phi += pi
    return [r, theta, phi]

'''
liste = [[1, 1, 1], [-1, 1, 1], [1, -1, 1], [-1, -1, 1], [1, 1, -1], [-1, 1, -1], [1, -1, -1], [-1, -1, -1]]
print("Running test:")
for a in liste:
    print(a, tocart(topol(a)))#, topol(a))
'''