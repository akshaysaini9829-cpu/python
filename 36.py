#36.	Horizontally stack [1,2,3] and [4,5,6]. Display the resulting shape.

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.hstack((a, b))

print(result)
print("Shape:", result.shape)