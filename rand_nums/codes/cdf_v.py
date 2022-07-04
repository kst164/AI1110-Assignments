import numpy as np
import matplotlib.pyplot as plt

NUM_INTERVALS = 100

u_arr = np.loadtxt("uni.dat", dtype="double")
v_arr = -2 * np.log(1 - u_arr)

buckets = np.linspace(-2, 8, num=NUM_INTERVALS)
freqs = []

for i in range(NUM_INTERVALS):
    freqs.append(np.sum(v_arr < buckets[i]) / len(v_arr))

theoretical = np.where(buckets < 0, 0, 1 - np.exp(-buckets/2))

plt.plot(buckets, freqs, 'o', label='Experimental')
plt.plot(buckets, theoretical, '-', label='Theoretical')
plt.legend()
plt.savefig('../figs/cdf_v.png')
plt.show()
