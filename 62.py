#62.	Given sales = [500, 1200, 2500, 800, 3000, 1500], categorize them as High (>=2500), Medium (>=1000), and Low (<1000).

import numpy as np

sales = np.array([500, 1200, 2500, 800, 3000, 1500])

conditions = [
    sales >= 2500,
    sales >= 1000
]

choices = ["High", "Medium"]

result = np.select(conditions, choices, default="Low")

print(result)