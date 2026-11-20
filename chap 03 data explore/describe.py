import pandas as pd
data = {
  "Name": ["Hamza", "Bilal", "Abdullah", "Nabeel", "Osama", "Nazim"],
  "Age": [23, 20, 21, 24, 26, 21],
  "Salary": [50000, 60000, 55000, 45000, 51000, 35000],
  "PerformenceScore": [90, 88, 85, 92, 95, 80]
}
df = pd.DataFrame(data)
print(df)
print(df.describe())


# 41:10