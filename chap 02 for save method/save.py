# import pandas as pd

# data = {
#   "Name": ['Hamza', 'Nabeel', 'Abdullah'],
#   "Age": [23, 24, 22],
#   "City": ['Karachi', 'Lahore', 'Hyderabad']
# }
# df = pd.DataFrame(data)
# print(df)

# df.to_csv("output.csv", index=0)





import pandas as pd

data = {
  "Name": ['Hamza', 'Nabeel', 'Abdullah'],
  "Age": [23, 24, 22],
  "City": ['Karachi', 'Lahore', 'Hyderabad']
}
df = pd.DataFrame(data)
print(df)

df.to_json("output.json", index=0)