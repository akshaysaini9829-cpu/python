#95.	Create an array, create a view using slicing, modify the view, and observe the original array.

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

view = arr[1:4]

view[0] = 100

print("Original array:", arr)
print("View:", view)