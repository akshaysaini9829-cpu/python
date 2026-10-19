#97.	Given a NumPy array, convert it into a Python list.

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

result = arr.tolist()

print("Python list:", result)