#45.	Given marks = [50, 55, 60, 65, 70], calculate variance and standard deviation.

import numpy as np

marks = np.array([50, 55, 60, 65, 70])

variance = np.var(marks)
std = np.std(marks)

print("Variance:", variance)
print("Standard Deviation:", std)