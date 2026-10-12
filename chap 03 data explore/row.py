import pandas as pd
df = pd.read_csv("ML.csv", encoding="latin1")
# print("display 2 rows of first")
# print(df.head(2))

# print("display 2 rows of end")
# print(df.tail(2))


print("display 2 rows of first")
print(df.head())

print("display 2 rows of end")
print(df.tail())