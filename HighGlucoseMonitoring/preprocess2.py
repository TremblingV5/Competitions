import shutil

import pandas as pd
import os


def merge(item, path):
    acc = pd.read_csv(os.path.join(path, f"ACC_{item}_grouped.csv"))
    bvp = pd.read_csv(os.path.join(path, f"BVP_{item}_grouped.csv"))
    eda = pd.read_csv(os.path.join(path, f"EDA_{item}_grouped.csv"))
    hr = pd.read_csv(os.path.join(path, f"HR_{item}_grouped.csv"))
    ibi = pd.read_csv(os.path.join(path, f"IBI_{item}_grouped.csv"))
    temp = pd.read_csv(os.path.join(path, f"TEMP_{item}_grouped.csv"))
    dexcom = pd.read_csv(os.path.join(path, f"Dexcom_{item}_grouped.csv"))
    food_log = pd.read_csv(os.path.join(path, f"Food_Log_{item}_grouped.csv"))

    df_list = [
        acc, bvp, eda, hr, ibi, temp
    ]

    for table in df_list:
        dexcom = pd.merge(dexcom, table, how='left', on=['timestamp_1'])

    dexcom['hr'].fillna(60 / dexcom['ibi'], inplace=True)
    dexcom['ibi'].fillna(60 / dexcom['hr'], inplace=True)

    dexcom = dexcom[dexcom['hr'].notnull() & dexcom['ibi'].notnull()]

    dexcom = pd.merge(dexcom, food_log, how='outer', on=['timestamp_1'])
    dexcom = dexcom.sort_values('timestamp_1')

    dexcom['timestamp_1'] = pd.to_datetime(dexcom['timestamp_1'], format='ISO8601')
    dexcom['last_food_interval'] = 0

    last_index = -1
    for i, row in dexcom.iterrows():
        if pd.notna(row['calorie']):
            last_index = i

        if last_index >= 0:
            last_food_interval = row['timestamp_1'] - dexcom.loc[last_index, 'timestamp_1']
            dexcom.at[i, 'last_food_interval'] = last_food_interval.seconds


    dexcom['calorie'].fillna(method='ffill', inplace=True)
    dexcom['total_carb'].fillna(method='ffill', inplace=True)
    dexcom['dietary_fiber'].fillna(method='ffill', inplace=True)
    dexcom['sugar'].fillna(method='ffill', inplace=True)
    dexcom['protein'].fillna(method='ffill', inplace=True)
    dexcom['total_fat'].fillna(method='ffill', inplace=True)

    dexcom = dexcom[dexcom['hr'].notnull() & dexcom['ibi'].notnull() & dexcom['calorie'].notnull()]
    dexcom = dexcom.iloc[:, 1:]

    dexcom.to_csv(os.path.join(path, f"treated.csv"), index=None)

    print(f"Finish: {folder}")


if __name__ == "__main__":
    path = r"D:\Project\Competitions\HighGlucoseMonitoring\source_data"

    # for folder in os.listdir(path):
    #     merge(folder, os.path.join(path, folder))

    for folder in os.listdir(path):
        target = os.path.join(path, folder, "treated.csv")
        if os.path.exists(target):
            shutil.copyfile(target, os.path.join(f"./data/{folder}.csv"))
