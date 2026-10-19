#24.	Reshape np.arange(1, 13) into 4 × 3 and then reshape it back into 2 × 6.

import numpy as np

arr = np.arange(1, 13)

# Reshape into 4 × 3
arr_4x3 = arr.reshape(4, 3)
print("4 × 3:")
print(arr_4x3)

# Reshape back into 2 × 6
arr_2x6 = arr_4x3.reshape(2, 6)
print("2 × 6:")
print(arr_2x6)