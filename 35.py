#35.	Vertically stack [[1,2,3]] and [[4,5,6]].

import numpy as np

a = np.array([[1, 2, 3]])
b = np.array([[4, 5, 6]])

result = np.vstack((a, b))

print(result)