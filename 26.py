#26.	Convert a 3 × 4 matrix into a 1D array using ravel().

import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

result = arr.ravel()

print(result)

