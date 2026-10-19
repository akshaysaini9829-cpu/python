#63.	Given age = [12, 17, 22, 35, 65, 70], create Minor (<18), Adult (18–59), and Senior (>=60) categories using np.select().

import numpy as np

age = np.array([12, 17, 22, 35, 65, 70])

conditions = [
    age < 18,
    age < 60
]

choices = ["Minor", "Adult"]

result = np.select(conditions, choices, default="Senior")

print(result)