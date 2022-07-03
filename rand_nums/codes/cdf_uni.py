import numpy as np
import matplotlib.pyplot as plt

NUM_INTERVALS = 100

arr = np.loadtxt("uni.dat", dtype="double")

buckets = np.linspace(-2, 3, num=NUM_INTERVALS)
freqs = []

theoretical = np.where(buckets < 0, 0, buckets)
theoretical = np.where(buckets < 1, theoretical, 1)

for i in range(NUM_INTERVALS):
    freqs.append(np.sum(arr < buckets[i]) / len(arr))

plt.plot(buckets, freqs, 'o', label='Experimental')
plt.plot(buckets, theoretical, '-', label='Theoretical')
plt.legend()
plt.savefig('../figs/cdf_uni.png')
plt.show()
