#51.	Using the same array, find the maximum value from each row and minimum value from each column

import numpy as np

marks = np.array([
    [80, 75, 90],
    [65, 88, 70],
    [92, 85, 95]
])

max_each_row = np.max(marks, axis=1)
min_each_column = np.min(marks, axis=0)

print("Maximum of each row:", max_each_row)
print("Minimum of each column:", min_each_column)