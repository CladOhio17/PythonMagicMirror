import io
import urllib
from io import BytesIO
from tkinter import Grid, Image
import customtkinter
import requests
from PIL import Image, ImageTk


class View:

    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        # super().__init__(parent)

    def setup_gui(self):
        self.root.winfo_screenwidth()
        self.root.winfo_screenheight()
        Grid.rowconfigure(self.root, 0, weight=1)
        Grid.columnconfigure(self.root, 0, weight=1)
        Grid.columnconfigure(self.root, 2, weight=1)
        Grid.columnconfigure(self.root, 1, weight=3)
        self.weather_frame = customtkinter.CTkFrame(self.root)
        self.weather_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew", rowspan=8, columnspan=1)
        weather_frame1 = customtkinter.CTkFrame(self.root)
        weather_frame1.grid(row=0, column=3, padx=20, pady=20, sticky="nsew", rowspan=8, columnspan=1)
        weather_frame2 = customtkinter.CTkFrame(self.root, fg_color="transparent")
        weather_frame2.grid(row=0, column=2, padx=20, pady=20, sticky="nsew", rowspan=8, columnspan=1)
        #label = customtkinter.CTkLabel(self.weather_frame, text="CTkLabel", fg_color="blue")
        #label.grid(row=0, column=0, sticky="nsew",padx=20, pady=20)

    def update_weather(self, data):
        weather_box = customtkinter.CTkTextbox(self.weather_frame)
        weather_text = (
               "City: {city}\n"
               "Date: {date}\n"
               "Temperature: {temperature}\u2103\n"
               "Wind: {wind} km/h\n"
               "Precipitation: {precipitation} mm\n"
               "Feels Like: {feelsLike}\u2103\n"
               "Weather Report: {sky}\n"
               ).format(city=data['city'], date=data['date'], temperature=data['temperature'], wind=data['wind'],
                        precipitation=data['precipitation'],feelsLike=data['feelsLike'], sky=data['sky'])
        weather_icon = customtkinter.CTkFrame(self.weather_frame, width=300, height=300)
        raw_data = urllib.request.urlopen("https:"+data['icon']).read()

        self.root.im = Image.open(io.BytesIO(raw_data))
        self.root.im = self.root.im.resize((300,300))

        self.root.icon = customtkinter.CTkImage(dark_image=self.root.im, size=(300,300))
        weather_icon.grid(row=0, column=0)
        label = customtkinter.CTkLabel(weather_icon, image=self.root.icon, text="")
        label.pack()
        weather_box.grid(row=0, column=1, sticky="nsew",columnspan=1,rowspan=8)
        weather_box.insert("0.0",weather_text)
        weather_box.configure(state="disabled")

