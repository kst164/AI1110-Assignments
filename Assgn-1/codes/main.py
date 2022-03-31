import matplotlib.pyplot as plt
import numpy as np

MONTHLY_DEPOSIT = 1000
INTEREST_RATE = 10
FINAL_INTEREST = 5550

# Monthly deposit, annual interest rate, number of months to maturity
def interest(deposit, rate, months):
    return deposit * months * (months + 1) * rate / (12 * 2 * 100)

input_space = np.array(range(100)) # Assuming less than 100 months
print(input_space)

output_space = interest(MONTHLY_DEPOSIT, INTEREST_RATE, input_space)
print(output_space)

# Interest over time
plt.plot(input_space, output_space)

# Final interest, i.e., y=FINAL_INTEREST
plt.plot(input_space, [FINAL_INTEREST for i in range(len(input_space))])

# We want point of intersection of the two plots


# Values chosen for visibility
plt.xlim(30, 40)
plt.ylim(3000, 7000)

plt.xlabel("Time (in months)")
plt.ylabel("Interest (in rupees)")
plt.grid()
plt.show()
