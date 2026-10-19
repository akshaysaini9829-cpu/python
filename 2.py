#2.	Create a 3 × 4 NumPy array containing numbers from 1 to 12. Display its shape and total number of elements.
import numpy as np

arr = np.arange(1, 13).reshape(3, 4)

print(arr)
print("Shape:", arr.shape)
print("Total elements:", arr.size)