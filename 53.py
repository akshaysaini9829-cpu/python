#53.	Sort the same array in descending order.

import numpy as np

arr = np.array([40, 10, 80, 30, 60, 20])

result = np.sort(arr)[::-1]

print("Descending order:", result)