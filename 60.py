#60.	Given sales = [500, 1200, 2500, 800, 3000], create an array containing 'High' for sales >= 2000 and 'Low' otherwise.

import numpy as np

sales = np.array([500, 1200, 2500, 800, 3000])

result = np.where(sales >= 2000, "High", "Low")

print(result)