#94.	Create an array, make a copy using copy(), modify the copy, and check whether the original changes.

import numpy as np

arr = np.array([10, 20, 30, 40])

copy_arr = arr.copy()

copy_arr[0] = 100

print("Original array:", arr)
print("Copied array:", copy_arr)