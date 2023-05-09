import customtkinter
import requests
from view.mirror_gui import View
from model.weather_model import WeatherModel

BASE_WEATHER_URL = "http://api.weatherapi.com/v1/current.json?key="


class Controller:

    def __init__(self):
        customtkinter.set_appearance_mode("dark")
        self.root = customtkinter.CTk()
        self.state = False
        self.model_weather = WeatherModel()
        self.view = View(self.root, self)
        self.URL = ""

    def get_weather(self):
        with open('weatherAPI.txt', 'r') as file:
            api_key = file.read().replace('\n', '')

        self.URL = BASE_WEATHER_URL + api_key + "&q=auto:ip"
        response = requests.get(self.URL)
        print(self.URL)

        if response.status_code == 200:
            data = response.json()
            self.model_weather.set_data(data)
        else:
            # showing the error message
            print("Error in the HTTP request:")
            print(response.status_code)

        self.update_weather()

    def __call__(self):

        self.root.title("Magic Mirror")
        self.root.bind("<F11>", self.toggle_fullScreen)
        self.root.bind("<Escape>", self.end_fullScreen)
        self.view.setup_gui()
        self.update_timer()
        self.root.mainloop()

    def toggle_fullScreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.root.attributes("-fullscreen", self.state)
        return "break"

    def end_fullScreen(self, event=None):
        self.state = False
        self.root.attributes("-fullscreen", False)
        return "break"

    def update_timer(self):
        print("Updated Weather Task")
        self.get_weather()
        self.root.after(900000, self.update_timer)

    def update_weather(self):

        weather_data = self.model_weather.get_data()
        self.view.update_weather(weather_data)

