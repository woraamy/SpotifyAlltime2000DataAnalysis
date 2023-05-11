import pandas as pd


class SpotifyData:
    def __init__(self):
        self.original_df = pd.read_csv('dataset.csv')
        self.__df = self.original_df.iloc[:20001, :]
        self.__df.dropna()

        # self.__cleaned_df = self.original_df.copy()

    @property
    def df(self):
        return self.__df



