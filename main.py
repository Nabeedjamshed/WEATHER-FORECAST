from tkinter import *
import tkinter as tk
from turtle import width

from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

m = Tk()
m.title("Weather App")
m.geometry('890x470+300+200')
m.configure(bg='#3f92ff')
m.resizable(False, False)


def getweather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="your_app_name")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timezone.config(text=result)
    long_lat.config(text=f'{round(location.latitude), 4}°N, {round(location.longitude), 4}°E')

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime('%I:%M %p')
    clock.config(text=current_time)

    api="https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=ad6e4ad799bcb26d267de424771618f3"
    json_data=requests.get(api).json()
    
    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']

    t.config(text=(temp,'°C'))
    h.config(text=(humidity,'%'))
    p.config(text=(pressure,'hPa'))
    w.config(text=(wind,'m/s'))
    d.config(text=description)
    
    # temp=json_data['current']['temp']
    # print(temp)

image_icon = PhotoImage(file="Images/logo.png")
m.iconphoto(False, image_icon)

round_table = PhotoImage(file="Images/Rounded Rectangle 1.png")
Label(m, image=round_table, bg="#3f92ff").place(x=30, y=110)

label1 = Label(m, text='Temperature', font=('Helvetica', 11), fg='white', bg='#203243')
label1.place(x=50, y=120)

label2 = Label(m, text='Humidity', font=('Helvetica', 11), fg='white', bg='#203243')
label2.place(x=50, y=140)

label3 = Label(m, text='Pressure', font=('Helvetica', 11), fg='white', bg='#203243')
label3.place(x=50, y=160)

label4 = Label(m, text='Wind Speed', font=('Helvetica', 11), fg='white', bg='#203243')
label4.place(x=50, y=180)

label5 = Label(m, text='Description', font=('Helvetica', 11), fg='white', bg='#203243')
label5.place(x=50, y=200)

search_image = PhotoImage(file="Images/Rounded Rectangle 3.png")
myimage = Label(m, image=search_image, bg='#57adff')
myimage.place(x=270, y=120)

cloud_image = PhotoImage(file='Images/Layer 7.png')
weather_image = Label(m, image=cloud_image, bg='#203243')
weather_image.place(x=290, y=127)

textfield = tk.Entry(m, justify='center', width=15, font=('poppins', 25, 'bold'), bg='#203243', fg='white', border=0)
textfield.place(x=370, y=130)
textfield.focus()

search_icon = PhotoImage(file='Images/Layer 6.png')
search_image = Button(image=search_icon, borderwidth=0, cursor='hand2', bg='#203243', command=getweather)
search_image.place(x=645, y=125)

frame = Frame(m, width=900, height=180, bg='#212120')
frame.pack(side=BOTTOM)

first_box = PhotoImage(file='Images/Rounded Rectangle 2.png')
second_box = PhotoImage(file='Images/Rounded Rectangle 2 copy.png')

Label(frame, image=first_box, bg='#212120').place(x=30, y=20)
Label(frame, image=second_box, bg='#212120').place(x=300, y=30)
Label(frame, image=second_box, bg='#212120').place(x=400, y=30)
Label(frame, image=second_box, bg='#212120').place(x=500, y=30)
Label(frame, image=second_box, bg='#212120').place(x=600, y=30)
Label(frame, image=second_box, bg='#212120').place(x=700, y=30)
Label(frame, image=second_box, bg='#212120').place(x=800, y=30)

clock = Label(m, font=('Helvetica', 30, 'bold'), fg='white', bg='#57adff')
clock.place(x=30, y=20)

timezone = Label(m, font=('Helvetica', 20), fg='white', bg='#57adff')
timezone.place(x=680, y=20)

long_lat = Label(m, font=('Helvetica', 10), fg='white', bg='#57adff')
long_lat.place(x=680, y=60)

t = Label(m, font=('Helvetica', 11), fg='white', bg='#203243')
t.place(x=150, y=120)

h = Label(m, font=('Helvetica', 11), fg='white', bg='#203243')
h.place(x=150, y=140)

p = Label(m, font=('Helvetica', 11), fg='white', bg='#203243')
p.place(x=150, y=160)

w = Label(m, font=('Helvetica', 11), fg='white', bg='#203243')
w.place(x=150, y=180)

d = Label(m, font=('Helvetica', 11), fg='white', bg='#203243')
d.place(x=150, y=200)
m.mainloop()
