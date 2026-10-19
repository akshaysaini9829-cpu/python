#64.	Extract all sales greater than 1500 from [1200, 850, 1500, 950, 2000, 1750, 1100].

import numpy as np

sales = np.array([1200, 850, 1500, 950, 2000, 1750, 1100])

result = sales[sales > 1500]

print("Sales greater than 1500:", result)