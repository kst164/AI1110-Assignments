import numpy as np
from scipy.special import erfc
import matplotlib.pyplot as plt

NUM_INTERVALS = 100

chi_sq_arr = np.loadtxt("chi_sq.dat", dtype="double")

buckets = np.linspace(-2, 8, num=NUM_INTERVALS)
freqs = []

def cdf(x):
    if x < 0:
        return 0.0
    else:
        return 1 - np.exp(-x/2)

vf = np.vectorize(cdf)
theoretical = vf(buckets)

# theoretical = (scipy.special.erf(buckets / np.sqrt(2)) + 1) / 2

for i in range(NUM_INTERVALS):
    freqs.append(np.sum(chi_sq_arr < buckets[i]) / len(chi_sq_arr))

plt.plot(buckets, freqs, 'o', label='Experimental')
plt.plot(buckets, theoretical, '-', label='Theoretical')
plt.legend()
plt.grid()
plt.savefig('../figs/cdf_chi.png')
plt.show()
