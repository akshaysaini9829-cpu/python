#48.	Given marks = [78, 91, 65, 88, 95], find the student position having the highest marks.

import numpy as np

marks = np.array([78, 91, 65, 88, 95])

position = np.argmax(marks)

print("Position of highest marks:", position)