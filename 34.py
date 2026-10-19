#34.	Concatenate two 1D arrays [10,20,30] and [40,50,60] into one array.

import numpy as np

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

result = np.concatenate((a, b))

print(result)