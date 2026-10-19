#71.	Find the unique values and their counts from [10,10,20,20,20,30,40,40].

import numpy as np

arr = np.array([10, 10, 20, 20, 20, 30, 40, 40])

values, counts = np.unique(arr, return_counts=True)

print("Unique values:", values)
print("Counts:", counts)