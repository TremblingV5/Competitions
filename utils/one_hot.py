from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pandas as pd


class OneHotBuilder:

    def __init__(self, data: pd.DataFrame, index):
        self.data = data
        self.index = index

    def set(self, column_name):
        print("ONE-HOT: " + column_name)
        temp = pd.Series(self.data[column_name].values, index=self.data[self.index])

        lb = LabelEncoder()
        x_pre = lb.fit_transform(temp)
        x_dict = dict([[i, j] for i, j in zip(temp, x_pre)])
        x_num = [[x_dict[i]] for i in temp]

        enc = OneHotEncoder()
        enc.fit(x_num)
        array_data = enc.transform(x_num).toarray()

        df = pd.DataFrame(array_data)
        inverse_dict = dict([val, key] for key, val in x_dict.items())
        df.columns = [column_name + "_" + str(inverse_dict[i]) for i in df.columns]

        self.data = self.data.drop(column_name, axis=1)
        self.data = pd.concat([self.data, df], axis=1)

        return self

    def build(self):
        return self.data
