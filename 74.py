#74.	Find the elements present in the first array but not in the second array.

import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([30, 40, 50, 60])

result = np.setdiff1d(a, b)

print("Elements only in first array:", result)