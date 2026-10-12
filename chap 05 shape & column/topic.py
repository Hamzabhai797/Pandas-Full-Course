import pandas as pd

data = {
  "name": ["hamza", "nabeel", "abdullah", "bilal", "maaz", "saifullah", "yaseen", "ghani"],
  "Age": [20, 21, 21, 23, 24, 25, 26, 27],
  "salary": [50000, 49000, 45000, 60000, 61000, 43000, 55000, 51000],
  "performance score": [85, 84, 81, 79, 75, 90, 89, 76] 
}

df = pd.DataFrame(data)
print(df)
print(f'Shape: {df.shape}')
print(f'columns Names: {df.columns}')