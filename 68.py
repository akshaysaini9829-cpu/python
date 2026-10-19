#68.	Check whether all values in [10, 20, 30, 40] are greater than 5.

import numpy as np

arr = np.array([10, 20, 30, 40])

result = np.all(arr > 5)

print("All values greater than 5:", result)