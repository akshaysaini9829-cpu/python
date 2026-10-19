#69.	Given marks = [65, 72, 81, 90], check whether all students scored at least 60 and whether any student scored above 85.

import numpy as np

marks = np.array([65, 72, 81, 90])

all_above_60 = np.all(marks >= 60)
any_above_85 = np.any(marks > 85)

print("All students scored at least 60:", all_above_60)
print("Any student scored above 85:", any_above_85)