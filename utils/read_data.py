import os.path

import pandas as pd
from sklearn.model_selection import train_test_split


class FileReader:
    def __init__(self, file_path_list, y, preprocess_list: list, test_size=0.3):
        for p in file_path_list:
            if os.path.exists(p):
                self.file_path = p
                break
        self.y = y
        self.test_size = test_size
        self.preprocess_list = preprocess_list

    def preprocess(self, data):
        for func in self.preprocess_list:
            data = func(data)

        col = data.pop(self.y)
        data.insert(len(data.columns), self.y, col)

        return data

    def read_no_seg(self):
        data = pd.read_csv(self.file_path)
        data = self.preprocess(data)

        x = data.iloc[:, :-1]
        y = data.iloc[:, -1]

        return x, y

    def read(self):
        data = pd.read_csv(self.file_path)
        data = self.preprocess(data)

        train_data, test_data = train_test_split(data, test_size=self.test_size)

        train_x = train_data.iloc[:, :-1]
        train_y = train_data.iloc[:, -1]
        test_x = test_data.iloc[:, :-1]
        test_y = test_data.iloc[:, -1]

        return train_x, train_y, test_x, test_y
