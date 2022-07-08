import numpy as np
from scipy.special import erfc
import matplotlib.pyplot as plt

NUM_INTERVALS = 100

gau_arr = np.loadtxt("gau.dat", dtype="double")
x1_arr, x2_arr = np.array_split(gau_arr, 2)

chi_arr = (x1_arr ** 2) + (x2_arr ** 2)

buckets = np.linspace(-2, 8, num=NUM_INTERVALS)
freqs = []

def pdf(x):
    if x < 0:
        return 0.0
    else:
        return np.exp(-x/2) / 2

vf = np.vectorize(pdf)
theoretical = vf(buckets)

for i in range(NUM_INTERVALS):
    freqs.append(np.sum(chi_arr < buckets[i]) / len(chi_arr))

slopes = []

for i in range(NUM_INTERVALS - 1):
    slopes.append((freqs[i+1] - freqs[i]) / (buckets[i+1] - buckets[i]))

plt.plot(buckets[:-1], slopes, 'o', label='Experimental')
plt.plot(buckets, theoretical, '-', label='Theoretical')
plt.legend()
plt.grid()
plt.savefig('../figs/pdf_chi.png')
plt.show()
