#17.	Using the same marks array, extract the value 88 and the complete last row.

import numpy as np

marks = np.array([
    [80, 75, 90],
    [65, 88, 70],
    [92, 85, 95]
])

print("Value 88:", marks[1, 1])
print("Last row:", marks[-1])