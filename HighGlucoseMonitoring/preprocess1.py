import typing

import pandas as pd

from util import path
import os

total_items = [
    # "ACC", "Dexcom", "EDA", "HR", "IBI", "TEMP"
    "BVP"
    # "Food_Log"
]

for folder in os.listdir(path):
    if "." in folder:
        continue

    if folder in []:
        continue

    for item in total_items:
        filename = os.path.join(path, folder, f"{item}_{folder}.csv")

        df: pd.DataFrame = pd.read_csv(filename)

        time_key: str = ""
        agg: typing.Dict = {}
        op = 'mean'

        if item == 'ACC':
            time_key = 'datetime'
            agg = {
                ' acc_x': op,
                ' acc_y': op,
                ' acc_z': op
            }
        elif item == 'BVP':
            time_key = 'datetime'
            agg = {
                ' bvp': op
            }
        elif item == 'Dexcom':
            time_key = 'Timestamp (YYYY-MM-DDThh:mm:ss)'
            agg = {
                'Glucose Value (mg/dL)': op,
                'Transmitter Time (Long Integer)': op
            }
        elif item == 'EDA':
            time_key = 'datetime'
            agg = {
                ' eda': op
            }
        elif item == 'Food_Log':
            time_key = 'time_begin'
            agg = {
                'calorie': 'sum',
                'total_carb': 'sum',
                'dietary_fiber': 'sum',
                'sugar': 'sum',
                'protein': 'sum',
                'total_fat': 'sum'
            }
        elif item == 'HR':
            time_key = 'datetime'
            agg = {
                ' hr': op
            }
        elif item == 'IBI':
            time_key = 'datetime'
            agg = {
                ' ibi': op
            }
        elif item == 'TEMP':
            time_key = 'datetime'
            agg = {
                ' temp': op
            }

        df['timestamp_1'] = df[time_key].apply(
            lambda x: str(x)[:19]
        )

        df = df.groupby('timestamp_1').agg(agg)

        for c in df.columns:
            df.rename(columns={c:c.strip()}, inplace=True)

        df.to_csv(os.path.join(path, folder, f"{item}_{folder}_grouped.csv"))
        print(f"{item}_{folder}_grouped.csv")
