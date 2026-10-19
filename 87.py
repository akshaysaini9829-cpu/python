#87.	Determine whether arrays with shapes (2,3) and (2,) can be broadcast together. Explain your answer.

import numpy as np

a = np.zeros((2, 3))
b = np.zeros(2)

try:
    result = a + b
    print("Arrays can be broadcast together.")
    print(result)
except ValueError:
    print("Arrays cannot be broadcast together.")