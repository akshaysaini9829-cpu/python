#32.	Split np.arange(1, 13) into 4 equal parts and display every part separately.

import numpy as np

arr = np.arange(1, 13)

parts = np.split(arr, 4)

print("Part 1:", parts[0])
print("Part 2:", parts[1])
print("Part 3:", parts[2])
print("Part 4:", parts[3])