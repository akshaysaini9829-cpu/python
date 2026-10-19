#91.	Given arr = [10, np.nan, 30, 40, np.nan, 60], identify which elements are missing and count them.

import numpy as np

arr = np.array([10, np.nan, 30, 40, np.nan, 60])

missing = np.isnan(arr)

print("Missing elements:", missing)
print("Number of missing elements:", np.sum(missing))