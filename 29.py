#29.	Transpose the matrix [[1, 2, 3], [4, 5, 6]] and display its new shape.

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

transpose = arr.T

print("Transpose:")
print(transpose)

print("New shape:", transpose.shape)