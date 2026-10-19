#92.	Calculate the mean and sum of an array containing np.nan values without allowing the missing values to affect the result.

import numpy as np

arr = np.array([10, np.nan, 30, 40, np.nan, 60])

mean = np.nanmean(arr)
total = np.nansum(arr)

print("Mean:", mean)
print("Sum:", total)
