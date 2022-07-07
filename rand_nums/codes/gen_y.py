import numpy as np

bernoulli_arr = np.loadtxt("ber.dat")
gaussian_arr = np.loadtxt("gau.dat", dtype=np.float64)

A = 0.5
y_arr = A * bernoulli_arr + gaussian_arr

np.savetxt("maxlike.dat", y_arr, "%.6f")
