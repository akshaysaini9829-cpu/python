#21.	From the same 3D array, extract the second row of the first 2D matrix.

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

result = arr[0, 1]

print(result)