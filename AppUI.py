import tkinter as tk
from tkinter import *
from tkinter import ttk
from DataProcessing import SpotifyData
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt
from GraphProcessing import GraphVis, HistogramVis, PieChartVis, ScatterPlot


class Application(tk.Tk):
    def __init__(self, data: SpotifyData):
        super().__init__()
        self.data = data.df
        # self.data = SpotifyData.df
        self.title("Spotify Top Tracks Analysis")
        # self.create_left_frame()
        self.create_left_frame()
        self.create_right_frame()
        self.graph = GraphVis(self.data)


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

    def create_buttons(self, graph):
        self.plotbutton = ttk.Button(self, text="Plot",
                                     command=self.plotting(graph))
        self.quitbutton = ttk.Button(self, text="Quit",
                                     command=self.destroy)
        self.backbutton = ttk.Button(self, text="Back")

    def create_graph_buttons(self):
        self.hist_button = ttk.Button(self.right_frame, text="Histogram", command=self.create_frame_hist)
        self.pie_button = ttk.Button(self.right_frame, text="Pie Chart", command=self.create_frame_pie)
        self.correlation_button = ttk.Button(self.right_frame, text="Correlation Graph",
                                             command=self.create_frame_scatter)
        self.network_button = ttk.Button(self.right_frame, text="Network Graph")
        self.hist_button.grid(row=1, column=1, padx=2)
        self.pie_button.grid(row=1, column=2, padx=2)
        self.correlation_button.grid(row=1, column=3, padx=2)
        self.network_button.grid(row=1, column=4, padx=2)

    def create_frame_hist(self):
        self.columns1 = ['popularity', 'duration_ms', 'duration_ms', 'danceability',
                   'energy', 'key', 'loudness', 'speechiness', 'acousticness',
                   'instrumentalness', 'liveness', 'valence', 'tempo',
                   'time_signature']
        self.hist_frame = LabelFrame(self.right_frame, text="Select Your Parameter")
        self.hist_frame.grid(row=2, column=1)
        self.cb_hist = ttk.Combobox(self.hist_frame, values=self.columns1, state="readonly")
        self.cb_hist.current(0)
        self.cb_hist.pack()
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

    def create_frame_pie(self):
        self.columns2 = ['explicit', 'key', 'mode', 'track_genre', 'time_signature']
        self.pie_frame = LabelFrame(self.right_frame, text="Select Your Parameter")
        self.cb_pie = ttk.Combobox(self.pie_frame, values=self.columns2)
        self.cb_pie.pack()

    def create_frame_scatter(self):
        self.columns3 = ['popularity', 'duration_ms', 'duration_ms', 'danceability',
                   'energy', 'key', 'loudness', 'speechiness', 'acousticness',
                   'instrumentalness', 'liveness', 'valence', 'tempo',
                   'time_signature']
        self.scatter_frame = LabelFrame(self.right_frame,
                                        text="Select Your Parameter")
        self.x_label = ttk.Label(self.scatter_frame,
                                 text="Select your x-axis")
        self.y_label = ttk.Label(self.scatter_frame,
                                 text="Select your y-axis")
        self.scatter_frame.grid(row=2, column=1)
        self.x_label.pack(side=LEFT)
        self.y_label.pack(side=LEFT)
        self.cb_x_scatter = ttk.Combobox(self.scatter_frame,
                                     values=self.columns3, state="readonly")
        self.cb_y_scatter = ttk.Combobox(self.scatter_frame,
                                     values=self.columns3, state="readonly")
        self.cb_x_scatter.pack(side=LEFT)
        self.cb_y_scatter.pack(side=LEFT)

    def plotting(self, graph):
        if graph == 'histogram':
            return HistogramVis(self.data, self.cb_hist.get()).plot
        elif graph == 'pie chart':
            return PieChartVis(self.data, self.cb_pie.get()).plot
        elif graph == 'scatter plot':
            return ScatterPlot(self.data, self.cb_x_scatter.get(),
                               self.cb_y_scatter.get()).plot
        elif graph == 'network':
            pass

    def run(self):
        self.mainloop()
