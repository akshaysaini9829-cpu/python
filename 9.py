#9.	Create an array from [10, 20, 30, 40] and check its data type before and after converting it to float.

import numpy as np

arr = np.array([10, 20, 30, 40])

print("Before:", arr.dtype)

float_arr = arr.astype(float)

print("After:", float_arr.dtype) 