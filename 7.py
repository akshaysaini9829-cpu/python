#7.	Create an integer array [10, 20, 30, 40] and convert it into a float array.

import numpy as np

arr = np.array([10, 20, 30, 40])

float_arr = arr.astype(float)

print(float_arr)