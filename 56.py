#56.	Use argsort() to display the top 3 values of sales = [1200, 850, 1500, 950, 2000].

import numpy as np

sales = np.array([1200, 850, 1500, 950, 2000])

indexes = np.argsort(sales)

top_3 = sales[indexes[-3:]][::-1]

print("Top 3 sales:", top_3)