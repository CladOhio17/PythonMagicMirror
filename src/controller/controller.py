import datetime
import time
import tkinter
import customtkinter
import requests
from view.mirror_gui import View
from model.weather_model import WeatherModel

BASE_WEATHER_URL = "http://api.weatherapi.com/v1/forecast.json?key="


class Controller:

    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        self.root = tkinter.Tk()
        self.state = False
        self.model_weather = WeatherModel()
        self.view = View(self.root, self)
        self.URL = ""
        self.t0 = time.time()
        return

    def get_weather(self):
        with open('weatherAPI.txt', 'r') as file:
            api_key = file.read().replace('\n', '')

        self.URL = BASE_WEATHER_URL + api_key + "&q=auto:ip&days=10"
        response = requests.get(self.URL)

        if response.status_code == 200:
            data = response.json()
            self.model_weather.set_data(data)
        else:
            # showing the error message
            print("Error in the HTTP request:")
            print(response.status_code)

        return

    def __call__(self):

        self.root.title("Magic Mirror")
        self.root.bind("<F11>", self.toggle_fullScreen)
        self.root.bind("<Escape>", self.end_fullScreen)
        self.get_weather()
        now = datetime.datetime.now()
        weather_data = self.model_weather.get_data()
        self.view.current_weather_gui(weather_data)
        self.view.forecast_gui(weather_data)
        self.update_timer()
        self.root.mainloop()
        return ""

    def toggle_fullScreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.root.attributes("-fullscreen", self.state)
        return "break"

    def end_fullScreen(self, event=None):
        self.state = False
        self.root.attributes("-fullscreen", False)
        return "break"

    def update_timer(self):
        now = datetime.datetime.now()
        current_day = now.strftime("%A")
        current_date = now.strftime("%B %d, %Y")
        self.model_weather.set_date(current_date, current_day)
        t1 = time.time()
        if t1 - self.t0 > 900:
            self.t0 = time.time()
            self.get_weather()
            self.view.update_weather()
            self.view.update_forecast()

        current_time_clock = now.strftime("%H:%M %p")
        self.model_weather.set_clock(current_time_clock)
        data = self.model_weather.get_data()
        self.view.update_clock(data)

        self.root.after(1, self.update_timer)


