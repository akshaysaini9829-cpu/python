#73.	Find the common elements between [10,20,30,40] and [30,40,50,60].

import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([30, 40, 50, 60])

common = np.intersect1d(a, b)

print("Common elements:", common)