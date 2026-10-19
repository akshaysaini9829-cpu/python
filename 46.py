#46.	Find the index of the smallest and largest value in [45, 12, 89, 34, 67].

import numpy as np

arr = np.array([45, 12, 89, 34, 67])

smallest_index = np.argmin(arr)
largest_index = np.argmax(arr)

print("Index of smallest value:", smallest_index)
print("Index of largest value:", largest_index)