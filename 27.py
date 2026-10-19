#27.	Create a 2D array, make a flattened copy using flatten() and a flattened view using ravel(), then modify one result and observe whether the original array changes.

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Create flattened copy and view
flat_copy = arr.flatten()
flat_view = arr.ravel()

# Modify both
flat_copy[0] = 100
flat_view[1] = 200

print("Original array:")
print(arr)

print("Flatten copy:")
print(flat_copy)

print("Ravel view:")
print(flat_view)