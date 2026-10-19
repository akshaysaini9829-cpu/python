#93.	Replace the missing values in [10, np.nan, 30, np.nan, 50] with the mean of the non-missing values.

import numpy as np

arr = np.array([10, np.nan, 30, np.nan, 50])

mean = np.nanmean(arr)

arr[np.isnan(arr)] = mean

print("Mean:", mean)
print("Result:", arr)