from AppUI import Application
from DataProcessing import SpotifyData
# from GraphProcessing import

if __name__ == '__main__':
    data_df = SpotifyData()
    app = Application(data_df)
    app.run()
