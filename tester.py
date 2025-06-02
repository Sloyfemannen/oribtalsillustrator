import probability as pr
import numpy as np
import matplotlib.pyplot as plt
from functions import PY, R
from scipy.integrate import simpson

A = np.array([0.6, 0.3, 0.1])

B = np.linspace(1, 3, 3)

#plt.bar(B, A)
#plt.plot()

a_0 = 1

x = np.linspace(0, 100*a_0, 1000)

theta = np.linspace(0, np.pi, 1000)
phi = np.linspace(0, 2*np.pi, 1000)
THETA, PHI = np.meshgrid(theta, phi)

for n in range(1, 7):
    for l in range(0, n):
        print(f"For n={n}, and l={l}, Simpson's method predicts: ", simpson(R(x, n, l)**2 * x**2, x))
        print()

for l in range(7):
    for m in range(-l, l+1):
        Y = PY(l, m, THETA, PHI)
        integrand = np.abs(Y)**2 * np.sin(THETA)
        print("Y: Simpson's method predicts: ", simpson(simpson(integrand, phi, axis=0), theta))
        print()