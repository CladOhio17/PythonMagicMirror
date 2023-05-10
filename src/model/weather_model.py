class WeatherModel:

    def __init__(self):
        self.forecast_day = None
        self.forecast = None
        self.current_temperature = None
        self.current_date = None
        self.current_day = None
        self.current_time = None
        self.wind = None
        self.precipitation = None
        self.feelsLike = None
        self.location = None
        self.city = None
        self.report = None
        self.sky = None
        self.icon = None
        self.date = None
        self.current = None

    def set_data(self, data):
        self.current = data['current']
        self.current_temperature = int(self.current['temp_c'])
        self.wind = self.current['wind_kph']
        self.precipitation = self.current['precip_mm']
        self.feelsLike = int(self.current['feelslike_c'])
        self.location = data['location']
        self.city = self.location['name']
        self.report = self.current['condition']
        self.sky = self.report['text']
        self.date = self.location['localtime']
        self.icon = self.report['icon']
        self.forecast = data['forecast']
        self.forecast_day = self.forecast['forecastday']

    def get_data(self):
        return {
            'wind': self.wind,
            'current_temperature': self.current_temperature,
            'precipitation': self.precipitation,
            'feelsLike': self.feelsLike,
            'location': self.location,
            'city': self.city,
            'report': self.report,
            'sky': self.sky,
            'icon': self.icon,
            'date': self.date,
            'current': self.current,
            'current_time': self.current_time,
            'current_day': self.current_day,
            'current_date': self.current_date,
            'forecastday': self.forecast_day
        }

    def set_clock(self, time):
        self.current_time = time

    def set_date(self, date, day):
        self.current_date = date
        self.current_day = day

    def get_clock(self):
        return self.current_time

    def get_date(self):
        return self.current_date

    def get_variable(self, variable):
        data = self.get_data()
        return data[variable]
