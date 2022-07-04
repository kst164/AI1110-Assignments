import numpy as np
import matplotlib.pyplot as plt

NUM_INTERVALS = 100

arr = np.loadtxt("uni.dat", dtype="double")

buckets = np.linspace(-2, 3, num=NUM_INTERVALS)
freqs = []

def pdf(x):
    if x > 0 and x < 1:
        return 1
    else:
        return 0

vf = np.vectorize(pdf)

# theoretical = np.where(np.logical_and(buckets > 0, buckets < 1), 1, 0)
theoretical = vf(buckets)

for i in range(NUM_INTERVALS):
    freqs.append(np.sum(arr < buckets[i]) / len(arr))

slopes = []

for i in range(NUM_INTERVALS - 1):
    slopes.append((freqs[i+1] - freqs[i]) / (buckets[i+1] - buckets[i]))

plt.plot(buckets[:-1], slopes, 'o', label='Experimental')
plt.plot(buckets, theoretical, '-', label='Theoretical')
plt.legend()
plt.grid()
plt.savefig('../figs/pdf_uni.png')
plt.show()
