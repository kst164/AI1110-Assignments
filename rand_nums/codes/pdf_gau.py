import numpy as np
import matplotlib.pyplot as plt

NUM_INTERVALS = 100

arr = np.loadtxt("gau.dat", dtype="double")

buckets = np.linspace(-6, 6, num=NUM_INTERVALS)
freqs = []

theoretical = np.exp(-buckets * buckets / 2) / np.sqrt(2 * np.pi)

for i in range(NUM_INTERVALS):
    freqs.append(np.sum(arr < buckets[i]) / len(arr))

slopes = []

for i in range(NUM_INTERVALS - 1):
    slopes.append((freqs[i+1] - freqs[i]) / (buckets[i+1] - buckets[i]))

plt.plot(buckets[:-1], slopes, 'o', label='Experimental')
plt.plot(buckets, theoretical, '-', label='Theoretical')
plt.legend()
plt.savefig('../figs/pdf_gau.png')
plt.show()
