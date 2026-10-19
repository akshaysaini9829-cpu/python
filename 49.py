#49.	Given marks = np.array([[80,75,90],[65,88,70],[92,85,95]]), calculate the total of each row.

import numpy as np

marks = np.array([
    [80, 75, 90],
    [65, 88, 70],
    [92, 85, 95]
])

row_total = np.sum(marks, axis=1)

print("Total of each row:", row_total)