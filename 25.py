#25.	Convert a 3 × 4 matrix into a 1D array using flatten().

import numpy as np

a = np.array([[ 1, 2, 3, 4],
            [ 5, 6 ,7 ,8],
            [ 9,10,11,12]])

b = a.flatten()

print(b)