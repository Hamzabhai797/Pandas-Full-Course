import pandas as pd

data = {
  "Name": ["Hamza", "Bilal", "Nabeel", "Abdullah", "Osama", "Maaz", "Saif"],
  "Age": [23, 20, 24, 21, 25, 21, 22],
  "Salary": [50000, 45000, 55000, 52000, 58000, 60000, 62000],
  "performanceScore": [85, 65, 75, 74, 73, 88, 87]
}
df = pd.DataFrame(data)
print(df)

df.loc[1, 'Salary'] = 48000
# df.loc[1, 'performanceScore'] = 70
print(df)