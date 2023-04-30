import inline as inline
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class CommonGraphVis:
    def __init__(self, data_df: pd.DataFrame, x_axis, y_axis):
        self.data_df = data_df
        self.x_axis = x_axis
        self.y_axis = y_axis

    def plot(self):
        pass


class PieChartVis(CommonGraphVis):
    def __init__(self, data_df, x_axis, y_axis):
        super().__init__(data_df, x_axis, y_axis)

    def plot(self):
        pass
