#23.	Create an array from 1 to 24 and reshape it into a 2 × 3 × 4 array.

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print(arr)