import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Read input
table = pd.read_excel("../tables/data.xlsx", skiprows=2, header=None).to_numpy()
ranges = table[:, 0]   # ["0-10", "10-20", ...]
sectionA = table[:, 1] # Frequency counts
sectionB = table[:, 3] # Frequency counts

# Make array of midpoints of ranges
bounds = np.array([r.split("-") for r in ranges], dtype="int32")
lower_bounds = bounds[:, 0]
upper_bounds = bounds[:, 1]
midpoints = (lower_bounds + upper_bounds) / 2

# For a frequency polygon, need to add zeroes to the left and right

# Find x coords of zeroes to prepend/append
first_interval = midpoints[1] - midpoints[0]
last_interval = midpoints[-1] - midpoints[-2]
first = midpoints[0] - first_interval
last = midpoints[-1] + last_interval

# Prepend/append zeroes
sectionA = np.concatenate(([0], sectionA, [0]))
sectionB = np.concatenate(([0], sectionB, [0]))
midpoints = np.concatenate(([first], midpoints, [last]))

# Plot aesthetics

# Make y axis show integers only
ax = plt.figure().gca()
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

plt.xlabel("Marks Obtained")
plt.ylabel("Number of Students")

plt.plot(midpoints, sectionA, '-o', label="Section A")
plt.plot(midpoints, sectionB, '-o', label="Section B")

# Start y axis at zero
# has to be after plt.plot because setting ylim disables autoscaling
plt.ylim(bottom=0)

plt.legend()
plt.show()
