import json
import pandas as pd

with open("./result.json", "r") as f:
    data = json.load(f)

results = data.get("results") # This is a list of python dictionaries

extras = []

# Removing the extra column dictionary from each result dictionary and adding it in a separate list
for row in results:
    extras.append(row.pop("extra"))

df1 = pd.DataFrame(results)
df2 = pd.DataFrame(extras)

result_df = pd.concat([df1, df2], axis=1, join="inner")
result_df.to_excel("result.xlsx")
