#8.	Create a float array [10.5, 20.8, 30.2] and convert it into an integer array. Observe the result.

import numpy as np

arr = np.array([10.5, 20.8, 30.2])

int_arr = arr.astype(int)

print(int_arr)