#33.	Given a 3 × 4 matrix, split it column-wise into 2 equal parts.

import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

parts = np.split(arr, 2, axis=1)

print("Part 1:")
print(parts[0])

print("Part 2:")
print(parts[1])