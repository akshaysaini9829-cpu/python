#58.	Given marks = [45, 78, 32, 90, 66], find the indexes where marks are greater than 60.

import numpy as np

marks = np.array([45, 78, 32, 90, 66])

indexes = np.where(marks > 60)[0]

print("Indexes:", indexes)