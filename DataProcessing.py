import pandas as pd


class SpotifyData:
    def __init__(self):
        self.original_df = pd.read_csv('dataset.csv')
        self.__cleaned_df = self.original_df.copy()


