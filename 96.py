#96.	Explain with code why copy() and a view behave differently.

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Copy
copy_arr = arr.copy()
copy_arr[0] = 100

# View using slicing
view_arr = arr[1:4]
view_arr[0] = 200

print("Original array:", arr)
print("Copy:", copy_arr)
print("View:", view_arr)