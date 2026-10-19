#18.	Extract the first two rows and last two columns from the marks array.

import numpy as np

marks = np.array([
    [80, 75, 90],
    [65, 88, 70],
    [92, 85, 95]
])

result = marks[:2, -2:]

print(result)