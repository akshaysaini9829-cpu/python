#67.	Check whether any value in [10, 20, 35, 40] is greater than 30.

import numpy as np

arr = np.array([10, 20, 35, 40])

result = np.any(arr > 30)

print("Any value greater than 30:", result)