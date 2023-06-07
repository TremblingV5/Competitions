import pandas as pd
import os
import time
import json

import typing

from utils.decorators import time_it

mid_path = r"D:\Code\Python\glucose-preprocess\mid"


@time_it
def read_csv(path) -> pd.DataFrame:
    return pd.read_csv(path)


def date_time2timestamp(date_time: str):
    return date_time.replace(" ", "_").replace(":", "~")


def get_info(date_time: str, path=mid_path) -> dict:
    if not os.path.exists(os.path.join(path, date_time2timestamp(date_time))):
        return {}
    with open(os.path.join(path, date_time), "r", encoding="utf-8") as f:
        info = f.read()

    return json.loads(info)


def write_info(date_time: str, data: typing.Dict, path=mid_path):
    with open(os.path.join(path, date_time2timestamp(date_time)), "w", encoding="utf-8") as f:
        f.write(json.dumps(data))


path = r"E:\BaiduNetdiskDownload\big-ideas-lab-glycemic-variability-and-wearable-device-data-1.1.0\big-ideas-lab" \
       r"-glycemic-variability-and-wearable-device-data-1.1.0"



demo_graphics = os.path.join(path, "Demographics.csv")

table_list = [
    "ACC", "BVP", "Dexcom", "EDA", "Food_Log", "HR", "IBI", "TEMP"
]

table_list = [
    "Dexcom", "EDA", "HR", "IBI", "TEMP"
]

for folder in os.listdir(path):
    if "." in folder:
        continue

    data_list = []

    for item in table_list:
        filename = os.path.join(
            path, folder, f"{item}_{folder}.csv"
        )

        df: pd.DataFrame = read_csv(filename)

        match item:
            case "Dexcom":
                df = pd.DataFrame(df, columns=['timestamp', 'Glucose Value (mg/dL)', 'Transmitter Time (Long Integer)'])
                df.rename(columns={"timestamp":"datetime"}, inplace=True)

        data_list.append(df)

    result = pd.concat(data_list)
    result.to_csv(f"{folder}_{item}.csv")
