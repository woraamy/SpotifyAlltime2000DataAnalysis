import tkinter as tk
from tkinter import *
from tkinter import ttk
from DataProcessing import SpotifyData
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt


class Application(tk.Tk):
    def __init__(self, data: SpotifyData):
        super().__init__()
        self.data = data
        # self.data = SpotifyData.df
        self.title("Spotify Top Tracks Analysis")
        # self.create_left_frame()
        self.create_left_frame()
        self.create_right_frame()

    def create_right_frame(self):
        self.right_frame = ttk.LabelFrame(self, text="Select Graph Type")
        self.right_frame.grid(row=0, column=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_graph_buttons()

    def create_left_frame(self):
        self.fig = plt.Figure(figsize=(5, 5))
        self.ax = self.fig.add_subplot
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(row=0, column=0)
        self.columnconfigure(0, weight=2)
        self.rowconfigure(0, weight=2)

    def create_graph_buttons(self):
        self.hist_button = ttk.Button(self.right_frame, text="Histogram", command=self.create_frame_hist)
        self.pie_button = ttk.Button(self.right_frame, text="Pie Chart", command=self.create_frame_pie)
        self.correlation_button = ttk.Button(self.right_frame, text="Correlation Graph", command=self.create_frame_corr)
        self.network_button = ttk.Button(self.right_frame, text="Network Graph")
        self.hist_button.grid(row=1, column=1, padx=2)
        self.pie_button.grid(row=1, column=2, padx=2)
        self.correlation_button.grid(row=1, column=3, padx=2)
        self.network_button.grid(row=1, column=4, padx=2)

    def create_frame_hist(self):
        columns = ['popularity', 'duration_ms', 'duration_ms', 'danceability',
                   'energy', 'key', 'loudness', 'speechiness', 'acousticness',
                   'instrumentalness', 'liveness', 'valence', 'tempo',
                   'time_signature']
        hist_frame = LabelFrame(self.right_frame, text="Select Your Parameter")
        hist_frame.grid(row=2, column=1)
        cb_hist = ttk.Combobox(hist_frame, values=columns, state="readonly")
        cb_hist.current(0)
        cb_hist.pack()
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

    def create_frame_pie(self):
        columns = ['explicit', 'key', 'mode', 'track_genre', 'time_signature']
        pie_frame = LabelFrame(self.right_frame, text="Select Your Parameter")
        cb_pie = ttk.Combobox(pie_frame, values=columns)
        cb_pie.pack()

    def create_frame_corr(self):
        columns = ['popularity', 'duration_ms', 'duration_ms', 'danceability',
                   'energy', 'key', 'loudness', 'speechiness', 'acousticness',
                   'instrumentalness', 'liveness', 'valence', 'tempo',
                   'time_signature']
        corr_frame = LabelFrame(self.right_frame, text="Select Your Parameter")
        x_label = ttk.Label(corr_frame, text="Select your x-axis")
        y_label = ttk.Label(corr_frame, text="Select your y-axis")
        corr_frame.grid(row=2, column=1)
        x_label.pack(side=LEFT)
        y_label.pack(side=LEFT)
        cb_x_pie = ttk.Combobox(corr_frame, values=columns, state="readonly")
        cb_y_pie = ttk.Combobox(corr_frame, values=columns, state="readonly")
        cb_x_pie.pack(side=LEFT)
        cb_y_pie.pack(side=LEFT)




    # def create_combobox_1(self, graph):
    #     if graph == 'histogram':
    #         self.cb_hist = ttk.Combobox(self.hist_frame)

    def run(self):
        self.mainloop()
