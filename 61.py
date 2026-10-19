#61.	Given marks = [95, 82, 74, 61, 45, 30], use np.select() to assign A+ for >=90, A for >=80, B for >=70, C for >=60, and Fail otherwise.

import numpy as np

marks = np.array([95, 82, 74, 61, 45, 30])

conditions = [
    marks >= 90,
    marks >= 80,
    marks >= 70,
    marks >= 60
]

choices = ["A+", "A", "B", "C"]

result = np.select(conditions, choices, default="Fail")

print(result)