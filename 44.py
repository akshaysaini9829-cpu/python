#44.	Compare the standard deviation of [10, 10, 10, 10] and [5, 15, 25, 35].

import numpy as np

a = np.array([10, 10, 10, 10])
b = np.array([5, 15, 25, 35])

std_a = np.std(a)
std_b = np.std(b)

print("Standard Deviation of A:", std_a)
print("Standard Deviation of B:", std_b)