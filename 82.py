#82.	Insert 25 at index 2 in [10,20,30,40,50].

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

result = np.insert(arr, 2, 25)

print("Result:", result)