import tkinter as tk
from DataProcessing import SpotifyData


class Application(tk.Tk):
    def __init__(self, data_df):
        super().__init__()
        self.title("Spotify Top Tracks Analysis")
        self.geometry("1000x700")

    def run(self):
        self.mainloop()
