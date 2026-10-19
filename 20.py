#20.	From the same 3D array, extract the first 2D matrix.

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

first_matrix = arr[0]

print(first_matrix)
