#19.	Create a 3D array using numbers 1 to 24 with shape (2, 3, 4). Access the element at index [1, 2, 3].

import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print(arr)
print("Element:", arr[1, 2, 3])
