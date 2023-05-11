import inline as inline
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from DataProcessing import SpotifyData


class GraphVis:
    def __init__(self, data: SpotifyData):
        self.data = data.df.copy()

    def plot(self):
        pass


class PieChartVis(GraphVis):
    def __init__(self, data: SpotifyData, index):
        super().__init__(data)
        self.index = index

    def plot(self):
        df_new = self.data[self.index]
        df_index = df_new.groupby(self.index).size
        return plt.pie(df_index, labels=df_index.index,
                       autopct='%1.1f%%', startangle=90)


class HistogramVis(GraphVis):
    def __init__(self, data: SpotifyData, x_axis):
        super().__init__(data)
        self.x = x_axis

    def plot(self):
        return self.data.hist(column=self.x)


class ScatterPlot(GraphVis):
    def __init__(self, data:SpotifyData, x_axis, y_axis):
        super().__init__(data)
        self.x = x_axis
        self.y = y_axis

    def plot(self):
        return sns.relplot(data=self.data, x=self.x, y=self.y)
#
# class NetworkGraph:
#     def __init__(self, data:SpotifyData):
