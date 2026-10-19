#55.	Find the indexes that would sort [40, 10, 80, 30, 60, 20].

import numpy as np

arr = np.array([40, 10, 80, 30, 60, 20])

indexes = np.argsort(arr)

print("Indexes:", indexes)