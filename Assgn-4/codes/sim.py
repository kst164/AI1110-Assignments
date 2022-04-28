import numpy as np
from numpy.random import default_rng

N = 1 << 16

rng = default_rng()
arr = rng.integers(3, size=N)

vals, counts = np.unique(arr, return_counts=True)

print(f"Simulated {N} times")
print(f"P(X=0) (Y) = {counts[0]/N}")
print(f"P(X=1) (R) = {counts[1]/N}")
print(f"P(X=2) (B) = {counts[2]/N}")
