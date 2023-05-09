
class WeatherModel:

    def __init__(self):
        self.wind = None
        self.temperature = None
        self.precipitation = None
        self.feelsLike = None
        self.location = None
        self.city = None
        self.report = None
        self.sky = None
        self.icon = None
        self.date = None
        self.main = None

    def set_data(self, data):
        self.main = data['current']
        self.temperature = self.main['temp_c']
        self.wind = self.main['wind_kph']
        self.precipitation = self.main['precip_mm']
        self.feelsLike = self.main['feelslike_c']
        self.location = data['location']
        self.city = self.location['name']
        self.report = self.main['condition']
        self.sky = self.report['text']
        self.date = self.location['localtime']
        self.icon = self.report['icon']
        print(f"City: {self.city}")
        print(f"Date: {self.date}")
        print(f"Temperature: {self.temperature}\u2103")
        print(f"Wind: {self.wind} km/h")
        print(f"Precipitation: {self.precipitation} mm")
        print(f"Feels Like: {self.feelsLike}\u2103")
        print(f"Weather Report: {self.sky}")
        print(f"icon: {self.icon}")

    def get_data(self):
        return {
            'wind': self.wind,
            'temperature': self.temperature,
            'precipitation': self.precipitation,
            'feelsLike': self.feelsLike,
            'location': self.location,
            'city': self.city,
            'report': self.report,
            'sky': self.sky,
            'icon': self.icon,
            'date': self.date,
            'main': self.main
        }

    def get_variable(self, variable):
        data = self.get_data()
        return data[variable]
