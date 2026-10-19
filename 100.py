#100.	Given sales = [1200,850,1500,950,2000,1750,1100,2200,1350,1600], find total, average, minimum, and maximum sales.

import numpy as np

sales = np.array([1200, 850, 1500, 950, 2000, 1750, 1100, 2200, 1350, 1600])

print("Total Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Minimum Sales:", np.min(sales))
print("Maximum Sales:", np.max(sales))