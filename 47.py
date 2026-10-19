#47.	Given sales = [1200, 850, 1500, 950, 2000], find the index of the highest sale.

import numpy as np

sales = np.array([1200, 850, 1500, 950, 2000])

index = np.argmax(sales)

print("Index of highest sale:", index)