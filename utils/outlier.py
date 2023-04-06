import pandas as pd


class OutlierHandler:
    def __init__(self, data):
        self.data = data.copy()

    def solve(self, column_name, strategy):
        self.data[column_name] = strategy.solve(self.data, column_name)
        return self

    def build(self):
        return self.data


class Strategy:
    def __init__(self):
        pass

    def solve(self):
        return self.data


class FillNaByValueStrategy(Strategy):
    def __init__(self, value):
        self.value = value

    def solve(self, data, column):
        data = data[column].fillna(self.value)
        return data

