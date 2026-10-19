#80.	Round [10.49, 10.51, 20.75, 30.25] to the nearest integer.

import numpy as np

arr = np.array([10.49, 10.51, 20.75, 30.25])

result = np.round(arr)

print("Rounded values:", result)