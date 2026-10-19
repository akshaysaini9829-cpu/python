#13.	From arr = np.arange(1, 16), extract the first 5 elements, last 5 elements, and elements from index 4 to 9.

import numpy as np

arr = np.arange(1, 16)

print("First 5:", arr[:5])
print("Last 5:", arr[-5:])
print("Index 4 to 9:", arr[4:10])