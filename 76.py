#76.	Find the square root and square of every value in [4, 9, 16, 25].

import numpy as np

arr = np.array([4, 9, 16, 25])

square_root = np.sqrt(arr)
square = np.square(arr)

print("Square root:", square_root)
print("Square:", square)