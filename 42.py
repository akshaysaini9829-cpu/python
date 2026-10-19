#1.	Given student marks [45, 67, 89, 72, 91, 55], calculate the average and median marks.

import numpy as np

marks = np.array([45, 67, 89, 72, 91, 55])

average = np.mean(marks)
median = np.median(marks)

print("Average:", average)
print("Median:", median)