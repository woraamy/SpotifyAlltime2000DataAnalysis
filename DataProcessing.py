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

    def retrieve_data(self, graph):
        global columns
        if graph == "histogram" or graph == "correlation":
            columns = ['popularity', 'duration_ms', 'duration_ms', 'danceability',
                       'energy', 'key', 'loudness', 'speechiness', 'acousticness',
                       'instrumentalness', 'liveness', 'valence', 'tempo',
                       'time_signature']

        elif graph == 'piechart':
            columns = ['explicit', 'key', 'mode', 'track_genre', 'time_signature']

        # elif graph == 'network':
        #     self.artists = self.__df['artists'].str.split(';')
        # self.__df['artists'] = self.__df['artists'].str.split(";")
        return columns

    def find_data(self, data_x, data_y):
        return self.df[data_x], self.df[data_y]


SpotifyData()
