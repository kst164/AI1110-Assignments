import numpy as np
from scipy.special import erfc
import matplotlib.pyplot as plt

NUM_INTERVALS = 100

gau_arr = np.loadtxt("gau.dat", dtype="double")
x1_arr, x2_arr = np.array_split(gau_arr, 2)

ray_arr = np.sqrt((x1_arr ** 2) + (x2_arr ** 2))

buckets = np.linspace(-2, 8, num=NUM_INTERVALS)
freqs = []

def cdf(x):
    if x < 0:
        return 0.0
    else:
        return 1 - np.exp(-x**2 / 2)

vf = np.vectorize(cdf)
theoretical = vf(buckets)

# theoretical = (scipy.special.erf(buckets / np.sqrt(2)) + 1) / 2

for i in range(NUM_INTERVALS):
    freqs.append(np.sum(ray_arr < buckets[i]) / len(ray_arr))

plt.plot(buckets, freqs, 'o', label='Experimental')
plt.plot(buckets, theoretical, '-', label='Theoretical')
plt.legend()
plt.grid()
plt.savefig('../figs/cdf_ray.png')
plt.show()
