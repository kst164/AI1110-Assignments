import numpy as np
import scipy.special
import matplotlib.pyplot as plt

NUM_INTERVALS = 100

arr = np.loadtxt("gau.dat", dtype="double")

buckets = np.linspace(-6, 6, num=NUM_INTERVALS)
freqs = []

theoretical = (scipy.special.erf(buckets / np.sqrt(2)) + 1) / 2

for i in range(NUM_INTERVALS):
    freqs.append(np.sum(arr < buckets[i]) / len(arr))

plt.plot(buckets, freqs, 'o', label='Experimental')
plt.plot(buckets, theoretical, '-', label='Theoretical')
plt.legend()
plt.savefig('../figs/cdf_gau.png')
plt.show()
