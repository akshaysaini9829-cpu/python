#90.	Set the random seed to 42 and generate 5 random integers. Run the code again and explain why the result is the same.

import numpy as np

np.random.seed(42)

result = np.random.randint(1, 101, 5)

print(result)