import numpy as np
import matplotlib.pyplot as plt

NUM_INTERVALS = 100

y_arr = np.loadtxt("maxlike.dat", dtype="double")

plt.plot(range(y_arr.shape[0]), y_arr, 'o')
plt.grid(axis='y')
plt.savefig('../figs/scatter_y.png')
plt.show()
