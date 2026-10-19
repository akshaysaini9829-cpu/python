#16.	Given marks = np.array([[80, 75, 90], [65, 88, 70], [92, 85, 95]]), extract the second row and third column.

import numpy as np

marks = np.array([
    [80, 75, 90],
    [65, 88, 70],
    [92, 85, 95]
])

print("Second row:", marks[1])
print("Third column:", marks[:, 2])