#86.	Given a = [[1,2,3],[4,5,6]] and b = [10,20,30], add them using broadcasting.

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([10, 20, 30])

result = a + b

print("Result:")
print(result)