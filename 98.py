#98.	Given a Pandas-like table represented as a 2D structure, explain how a .values attribute would be used to obtain a NumPy array.

import pandas as pd

data = {
    "Name": ["Aman", "Ravi", "Neha"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

arr = df.values

print(arr)
print(type(arr))