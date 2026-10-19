#30.	Create a 3 × 4 matrix and convert it into a 4 × 3 matrix using transpose.
import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

transpose = arr.T

print("Original 3 × 4 matrix:")
print(arr)

print("\nTransposed 4 × 3 matrix:")
print(transpose)