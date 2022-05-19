from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

n = 4
p = 1/2

rv = binom(n, p)

x = np.arange((n + 1))

pmf = rv.pmf(x)

# plt.plot(x, pmf, 'ro')
plt.vlines(x, 0, pmf)

plt.xlabel("X (Number of heads)")
plt.ylabel("P(X = x) (probability of x heads)")
plt.show()
