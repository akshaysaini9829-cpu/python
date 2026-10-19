#38.	Given sales = [1200, 850, 1500, 950, 2000], find the total sales and highest sale.

import numpy as np

sales = np.array([1200, 850, 1500, 950, 2000])

print("Total Sales:", np.sum(sales))
print("Highest Sale:", np.max(sales))