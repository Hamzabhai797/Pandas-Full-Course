# import pandas as pd
# data = {
#   "name": ["Hamza", "bilal", "osama"],
#   "age": [20, 23, 25],
#   "city": ["karachi", "pindhi", "islamabad"]
# }
# df = pd.DataFrame(data)
# print(df)
# # df.to_csv("out.csv", index=False)
# # df.to_json("outpur.json", indent=False)
# df.to_excel("out.xlsx", index=False)




# import pandas as pd
# data = {
#   "name": ["Hamza", "bilal", "osama"],
#   "age": [20, 23, 25],
#   "city": ["karachi", "pindhi", "islamabad"]
# }
# df = pd.DataFrame(data)
# print(df)

import pandas as pd
data = {
  "name": ["Hamza", "nabeel", "khan"],
  "age": [20, 23, 25],
  "city": ["karachi", "pindhi", "islamabad"]
}
df = pd.DataFrame(data)
print(df)
df.to_html("out.html", index=False)