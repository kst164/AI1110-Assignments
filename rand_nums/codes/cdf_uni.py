import numpy as np
import matplotlib.pyplot as plt

NUM_INTERVALS = 100

arr = np.loadtxt("uni.dat", dtype="double")

buckets = np.linspace(-2, 3, num=NUM_INTERVALS)
freqs = []

def cdf(x):
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1

vf = np.vectorize(cdf, otypes=[np.float64])
theoretical = vf(buckets)

for i in range(NUM_INTERVALS):
    freqs.append(np.sum(arr < buckets[i]) / len(arr))

plt.plot(buckets, freqs, 'o', label='Experimental')
plt.plot(buckets, theoretical, '-', label='Theoretical')
plt.legend()
plt.savefig('../figs/cdf_uni.png')
plt.show()
