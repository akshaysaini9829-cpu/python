#50.	Using the same array, calculate the average of each column.

import numpy as np

marks = np.array([
    [80, 75, 90],
    [65, 88, 70],
    [92, 85, 95]
])

column_average = np.mean(marks, axis=0)

print("Average of each column:", column_average)