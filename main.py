
import numpy as np
import matplotlib.pyplot as plt
from coord_translation import topol, tocart
from functions import Mintegral, SMintegral

def f(x):
    return 1/(x+1)**2

mesh = np.linspace(0, 100, 1000)

fspace = f(mesh)

integ = SMintegral(f, mesh)

abs = fspace/integ

plt.plot(mesh, abs)
plt.plot(mesh, fspace)
plt.show()

