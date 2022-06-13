import numpy as np
from scipy.special import comb
import matplotlib.pyplot as plt

vals = np.arange(181)
probs = comb(180, vals) * ((1 / 3) ** vals) * ((2 / 3) ** (180 - vals))
cum_probs = np.cumsum(probs)

# Answer:
# print(cum_probs[70] - cum_probs[49])

plt.plot(vals, cum_probs)

plt.xlabel("Y (Number of calls in interval)")
plt.ylabel("F_Y(y)")
plt.show()
