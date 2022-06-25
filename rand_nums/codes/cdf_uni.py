import numpy as np
import matplotlib.pyplot as plt

NUM_INTERVALS = 100

arr = np.loadtxt("uni.dat", dtype="double")

buckets = np.linspace(-2, 3, num=NUM_INTERVALS)
freqs = []

for i in range(NUM_INTERVALS):
    freqs.append(np.sum(arr < buckets[i]) / len(arr))

plt.plot(buckets, freqs)
plt.savefig('../figs/cdf_uni.png')
plt.show()
