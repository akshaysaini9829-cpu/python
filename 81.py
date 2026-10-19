#81.	Calculate the mean of [78.456, 82.789, 91.234] and display the result rounded to 2 decimal places.

import numpy as np

arr = np.array([78.456, 82.789, 91.234])

mean = np.mean(arr)
result = np.round(mean, 2)

print("Mean:", result)