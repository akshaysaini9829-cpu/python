#89.	Generate a 3 × 3 array of random integers between 10 and 50.

import numpy as np

result = np.random.randint(10, 51, size=(3, 3))

print(result)