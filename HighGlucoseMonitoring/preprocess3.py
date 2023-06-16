import pandas as pd
import os


file_list = []

for filename in os.listdir("./data"):
    f = pd.read_csv(os.path.join("./data", filename))
    file_list.append(f)

total = pd.concat(file_list)

total["Y"] = total["Glucose Value (mg/dL)"].apply(lambda x: 1 if x > 140.4 else 0)

total.to_csv("./data/all.csv", index=False)
