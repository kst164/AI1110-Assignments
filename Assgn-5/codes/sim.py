import numpy as np
from numpy.random import default_rng

# Number of trials
N = 1 << 16

# reward for heads/tails in increments of Rs 0.5 (to use int8 instead of float)
heads_val = 2
tails_val = -3

rng = default_rng()
flips_arr = rng.integers(0x10, dtype=np.int8, size=N) # 4 bits, so each value is 4 coin flips

total_arr = np.zeros_like(flips_arr, dtype=np.int8)

for i in range(4):
    # result of ith flip
    flip_arr = (flips_arr >> i) & 1

    # heads if bit is set, else false
    total_arr += np.where(flip_arr, heads_val, tails_val)

vals, counts = np.unique(total_arr, return_counts=True)
vals = vals * 0.5
for i in range(len(vals)):
    print(f"P(X = {vals[i]:4}) = {counts[i]/N}")
