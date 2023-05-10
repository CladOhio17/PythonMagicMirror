import datetime
import io
import time
import urllib
from tkinter import Image, Canvas

import PIL
from PIL import Image, ImageTk


class View:

    def __init__(self, root, controller):
        self.im1 = None
        self.d1_icon = None
        self.day1_image = None
        self.current_perc = None
        self.current_feels = None
        self.current_sky = None
        self.start = None
        self.f_date = None
        self.d1 = None
        self.forecast = None
        self.f_day1 = None
        self.current_icon = None
        self.im = None
        self.current_image = None
        self.date_str = None
        self.canvas = None
        self.root = root
        self.controller = controller
        self.current_temp = None
        self.current_report = None

    def current_weather_gui(self, data):

        self.canvas = Canvas(self.root, bg="#000000", bd=0, highlightthickness=0, relief="ridge")
        self.canvas.pack(fill="both", expand=True)

        feelslike = "Feels Like: {t}\xb0".format(t=data['feelsLike'])
        self.root.current_feels = self.canvas.create_text(144.0, 144.0, anchor="nw", text=feelslike, fill="#FFFFFF",
                                                          font=("Inter Light", 24 * -1))

        precipitation = "Precipitation: {t}mm".format(t=data['precipitation'])
        self.root.current_perc = self.canvas.create_text(319.0, 144.0, anchor="nw", text=precipitation, fill="#FFFFFF",
                                                         font=("Inter Light", 24 * -1))

        self.root.current_sky = self.canvas.create_text(8, 144.0, anchor="nw", text=data['sky'], fill="#FFFFFF",
                                                        font=("Inter Light", 24 * -1))

        temp = "{t}\xb0".format(t=data['current_temperature'])
        self.root.current_temp = self.canvas.create_text(
            144.0, 48, anchor="nw", text=temp, fill="#FFFFFF", font=("Inter Light", 64 * -1))

        self.root.clock = self.canvas.create_text(
            272.0, 48.0, anchor="nw", text=data['current_time'], fill="#FFFFFF", font=("Inter Light", 64 * -1))

        self.date_str = "{name}\n{date}".format(name=data['current_day'], date=data['current_date'])
        self.root.date = self.canvas.create_text(
            272.0, 24, anchor="nw", text=self.date_str, fill="#FFFFFF", font=("Inter Light", 24 * -1))

        fp = ("" + data['icon'])
        fp = fp.replace('//cdn.weatherapi.com/','')

        self.im = PIL.Image.open(fp)
        self.im = self.im.resize((144, 144))
        self.current_image = PIL.ImageTk.PhotoImage(self.im)

        self.current_icon = self.canvas.create_image(
            -24,
            8,
            image=self.current_image,
            anchor="nw"
        )


    def update_clock(self, data):
        self.canvas.itemconfigure(self.root.clock, text=data['current_time'])
        self.date_str = "{name} {date}".format(name=data['current_day'], date=data['current_date'])

        self.canvas.itemconfigure(self.root.date, text=self.date_str)

    # TODO: add forecast to update
    # TODO: Change time from date time to model time
    def update_weather(self, data):

        # weather_icon = customtkinter.CTkFrame(self.weather_frame, width=300, height=300)
        #raw_data = urllib.request.urlopen("https:" + data['icon']).read()
        precipitation = "Precipitation: {t}mm".format(t=data['precipitation'])
        temp = "{t}\xb0".format(t=data['current_temperature'])
        feelslike = "Feels Like: {t}\xb0".format(t=data['feelsLike'])

        self.date_str = "{name}\n{date}".format(name=data['current_day'], date=data['current_date'])
        #self.im = Image.open(io.BytesIO(raw_data))
        #self.im = self.im.resize((144, 144))
        #self.current_image = Image.BitmapImage(self.im)
        fp = ("" + data['icon'])
        fp = fp.replace('//cdn.weatherapi.com/','')

        self.im = PIL.Image.open(fp)
        self.im = self.im.resize((128, 128))
        self.current_image = PIL.ImageTk.PhotoImage(self.im)
        self.canvas.itemconfigure(self.root.current_icon, image=self.current_image)
        self.canvas.itemconfigure(self.root.date, text=self.date_str)
        self.canvas.itemconfigure(self.root.current_sky, data['sky'])
        self.canvas.itemconfigure(self.root.current_temp, temp)
        self.canvas.itemconfigure(self.root.current_perc, precipitation)
        self.canvas.itemconfigure(self.root.current_feels, feelslike)

    def forecast_gui(self, data):
        self.forecast = data['forecastday']
        now = datetime.datetime.now()
        start = 0

        for x in self.forecast:
            start += 1
            t1 = time.strftime('%x', time.localtime(x['date_epoch']))
            t2 = now.strftime('%x')
            if t1 == t2:
                break

        # TODO: put this in a loop
        # TODO: Save Icons in a model

        d1 = self.forecast[start]
        day = d1['day']
        d2 = self.forecast[start + 1]
        day2 = d2['day']
        d3 = self.forecast[start + 2]
        day3 = d3['day']
        d4 = self.forecast[start + 3]
        day4 = d4['day']
        # Forecast Day 1:

        f_date = time.strftime('%a', time.localtime(d1['date_epoch']))
        temp_min = "{t}\xb0".format(t=day['mintemp_c'])
        temp_max = "{t}\xb0".format(t=day['maxtemp_c'])
        totalprecip_mm = "{t}mm".format(t=day['totalprecip_mm'])
        icon = day['condition']
        fp = ("" + icon['icon'])
        fp = fp.replace('//cdn.weatherapi.com/','')

        self.im1 = PIL.Image.open(fp)

        self.day1_image = PIL.ImageTk.PhotoImage(self.im1)
        self.d1_icon = self.canvas.create_image(
            72,
            256,
            image=self.day1_image,
            anchor="nw",
        )
        self.f_day1 = self.canvas.create_text(24, 272.0, anchor="nw", text=f_date, fill="#FFFFFF",
                                              font=("Inter Light", 24 * -1))
        self.canvas.create_text(144.0, 272.0, anchor="nw", text=temp_max, fill="#FFFFFF", font=("Inter Light", 24 * -1))
        self.canvas.create_text(208.0, 272.0, anchor="nw", text=temp_min, fill="#949494", font=("Inter Light", 24 * -1))
        self.canvas.create_text(271.0, 272.0, anchor="nw", text=totalprecip_mm, fill="#FFFFFF",
                                font=("Inter Light", 24 * -1))

        # Forecast Day 2:
        f_date = time.strftime('%a', time.localtime(d2['date_epoch']))
        temp_min = "{t}\xb0".format(t=day2['mintemp_c'])
        temp_max = "{t}\xb0".format(t=day2['maxtemp_c'])
        totalprecip_mm = "{t}mm".format(t=day2['totalprecip_mm'])

        icon = day2['condition']
        fp = ("" + icon['icon'])
        fp = fp.replace('//cdn.weatherapi.com/', '')

        self.im2 = PIL.Image.open(fp)

        self.day2_image = PIL.ImageTk.PhotoImage(self.im2)
        self.d2_icon = self.canvas.create_image(
            72,
            320,
            image=self.day2_image,
            anchor="nw",
        )
        self.canvas.create_text(24, 336.0, anchor="nw", text=f_date, fill="#FFFFFF", font=("Inter Light", 24 * -1))
        self.canvas.create_text(144.0, 336.0, anchor="nw", text=temp_max, fill="#FFFFFF", font=("Inter Light", 24 * -1))
        self.canvas.create_text(208.0, 336.0, anchor="nw", text=temp_min, fill="#949494", font=("Inter Light", 24 * -1))
        self.canvas.create_text(271.0, 336.0, anchor="nw", text=totalprecip_mm, fill="#FFFFFF",
                                font=("Inter Light", 24 * -1))

        # Forecast Day 3:

        f_date = time.strftime('%a', time.localtime(d3['date_epoch']))
        temp_min = "{t}\xb0".format(t=day3['mintemp_c'])
        temp_max = "{t}\xb0".format(t=day3['maxtemp_c'])
        totalprecip_mm = "{t}mm".format(t=day3['totalprecip_mm'])
        icon = day3['condition']
        fp = ("" + icon['icon'])
        fp = fp.replace('//cdn.weatherapi.com/', '')

        self.im3 = PIL.Image.open(fp)

        self.day3_image = PIL.ImageTk.PhotoImage(self.im3)
        self.d3_icon = self.canvas.create_image(
            72,
            384,
            image=self.day3_image,
            anchor="nw",
        )
        self.canvas.create_text(24, 400.0, anchor="nw", text=f_date, fill="#FFFFFF", font=("Inter Light", 24 * -1))
        self.canvas.create_text(144.0, 400.0, anchor="nw", text=temp_max, fill="#FFFFFF", font=("Inter Light", 24 * -1))
        self.canvas.create_text(208.0, 400.0, anchor="nw", text=temp_min, fill="#949494", font=("Inter Light", 24 * -1))
        self.canvas.create_text(271.0, 400.0, anchor="nw", text=totalprecip_mm, fill="#FFFFFF",
                                font=("Inter Light", 24 * -1))

        # Forecast Day 4:
        f_date = time.strftime('%a', time.localtime(d4['date_epoch']))
        temp_min = "{t}\xb0".format(t=day4['mintemp_c'])
        temp_max = "{t}\xb0".format(t=day4['maxtemp_c'])
        totalprecip_mm = "{t}mm".format(t=day4['totalprecip_mm'])
        icon = day2['condition']
        fp = ("" + icon['icon'])
        fp = fp.replace('//cdn.weatherapi.com/', '')

        self.im4 = PIL.Image.open(fp)

        self.day4_image = PIL.ImageTk.PhotoImage(self.im4)
        self.d4_icon = self.canvas.create_image(
            72,
            448,
            image=self.day2_image,
            anchor="nw",
        )

        self.canvas.create_text(24, 464.0, anchor="nw", text=f_date, fill="#FFFFFF", font=("Inter Light", 24 * -1))
        self.canvas.create_text(144.0, 464.0, anchor="nw", text=temp_max, fill="#FFFFFF", font=("Inter Light", 24 * -1))
        self.canvas.create_text(208.0, 464.0, anchor="nw", text=temp_min, fill="#949494", font=("Inter Light", 24 * -1))
        self.canvas.create_text(271.0, 464.0, anchor="nw", text=totalprecip_mm, fill="#FFFFFF",
                                font=("Inter Light", 24 * -1))

    def update_forecast(self):
        pass
