import numpy as np
from scipy.special import erfc
import matplotlib.pyplot as plt

NUM_INTERVALS = 100

chi_sq_arr = np.loadtxt("chi_sq.dat", dtype="double")

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
    freqs.append(np.sum(chi_sq_arr < buckets[i]) / len(chi_sq_arr))

slopes = []

for i in range(NUM_INTERVALS - 1):
    slopes.append((freqs[i+1] - freqs[i]) / (buckets[i+1] - buckets[i]))

plt.plot(buckets[:-1], slopes, 'o', label='Experimental')
plt.plot(buckets, theoretical, '-', label='Theoretical')
plt.legend()
plt.grid()
plt.savefig('../figs/pdf_chi.png')
plt.show()
