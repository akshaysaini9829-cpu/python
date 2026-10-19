#31.	Split np.arange(1, 13) into 3 equal parts.

import numpy as np

arr = np.arange(1, 13)

parts = np.split(arr, 3)

print(parts)