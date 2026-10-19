#54.	Sort each row of [[30,10,20],[90,60,70]] in ascending order.

import numpy as np

arr = np.array([
    [30, 10, 20],
    [90, 60, 70]
])

result = np.sort(arr, axis=1)

print(result)