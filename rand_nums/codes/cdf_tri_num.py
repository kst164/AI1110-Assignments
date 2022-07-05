import numpy as np
import matplotlib.pyplot as plt

NUM_INTERVALS = 100

arr = np.loadtxt("tri.dat", dtype="double")

buckets = np.linspace(-2, 4, num=NUM_INTERVALS)
freqs = []

for i in range(NUM_INTERVALS):
    freqs.append(np.sum(arr < buckets[i]) / len(arr))

plt.plot(buckets, freqs, 'o', label='Experimental')
plt.legend()
plt.grid()
plt.savefig('../figs/cdf_tri_num.png')
plt.show()
