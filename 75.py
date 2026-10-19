#75.	Find the union and symmetric difference of [1,2,3,4] and [3,4,5,6].

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([3, 4, 5, 6])

union = np.union1d(a, b)
symmetric_difference = np.setxor1d(a, b)

print("Union:", union)
print("Symmetric Difference:", symmetric_difference)