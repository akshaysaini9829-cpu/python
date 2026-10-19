#66.	Extract values that are either below 1000 or above 2000.

import numpy as np

sales = np.array([1200, 850, 1500, 950, 2000, 1750, 1100])

result = sales[(sales < 1000) | (sales > 2000)]

print("Values:", result)