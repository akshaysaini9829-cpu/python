#65.	Extract values between 1000 and 1800 from the same sales array.

import numpy as np

sales = np.array([1200, 850, 1500, 950, 2000, 1750, 1100])

result = sales[(sales >= 1000) & (sales <= 1800)]

print("Values between 1000 and 1800:", result)