import probability as pr
import numpy as np
import matplotlib.pyplot as plt

A = np.array([0.6, 0.3, 0.1])

B = np.linspace(1, 3, 3)

plt.bar(B, A)
plt.plot()