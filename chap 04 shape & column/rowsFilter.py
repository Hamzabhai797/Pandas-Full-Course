import pandas as pd

data = {
  "name": ["hamza", "nabeel", "abdullah", "bilal", "maaz", "saifullah", "yaseen", "ghani"],
  "Age": [20, 21, 21, 23, 24, 25, 26, 27],
  "salary": [50000, 49000, 45000, 60000, 61000, 43000, 55000, 51000],
  "performance score": [85, 84, 81, 79, 75, 90, 89, 76] 
}

df = pd.DataFrame(data)
print(df)

print("rows Filter")

# high_salary = df[df['salary'] > 50000]
# print(high_salary)


# Multiple conditions
# high_salary = df[(df['Age'] > 25) & (df['salary'] > 50000)]
# print(high_salary)


# using or condition
high_salary = df[(df['Age'] > 30) | (df['performance score'] > 80)]
print(high_salary)
