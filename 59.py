#59.	Replace all values below 40 in [25, 65, 35, 80, 45] with 0.

import numpy as np

arr = np.array([25, 65, 35, 80, 45])

arr[arr < 40] = 0

print(arr)