#39.	Given a 2D marks array, find the minimum and maximum marks from the complete array.

import numpy as np

marks = np.array([
    [80, 75, 90],
    [65, 88, 70],
    [92, 85, 95]
])

print("Minimum Marks:", np.min(marks))
print("Maximum Marks:", np.max(marks))