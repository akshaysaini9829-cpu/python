#72.	Given a product category array ['A','B','A','C','B','A'], find all unique categories.

import numpy as np

categories = np.array(['A', 'B', 'A', 'C', 'B', 'A'])

unique_categories = np.unique(categories)

print("Unique categories:", unique_categories)