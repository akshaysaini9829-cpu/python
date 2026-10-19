#41.	Find the mean and median of [10, 20, 20, 30, 100]. Compare the results.

import numpy as np

arr = np.array([10, 20, 20, 30, 100])

mean = np.mean(arr)
median = np.median(arr)

print("Mean:", mean)
print("Median:", median)