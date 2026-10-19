#57.	Use argsort() to arrange student marks in descending order while keeping their original indexes.\

import numpy as np

marks = np.array([78, 91, 65, 88, 95])

indexes = np.argsort(marks)[::-1]

print("Indexes:", indexes)
print("Marks:", marks[indexes])