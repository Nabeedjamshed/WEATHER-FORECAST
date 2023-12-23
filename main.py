from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
# from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

m = Tk()
m.title("Weather App")
m.geometry('890x470+300+200')
m.configure(bg='#3f92ff')
m.resizable(False,False)


image_icon = PhotoImage(file="Images/logo.png")
m.iconphoto(False, image_icon)

round_table = PhotoImage(file="Images/Rounded Rectangle 1.png")
Label(m, image=round_table,bg="#3f92ff").place(x=30,y=110)

label1 = Label(m, text='Temperature', font=('Helvetica',11),fg='white', bg='#203243')
label1.place(x=50, y=120)

label2 = Label(m, text='Humidity', font=('Helvetica',11),fg='white', bg='#203243')
label2.place(x=50, y=140)

label3 = Label(m, text='Pressure', font=('Helvetica',11),fg='white', bg='#203243')
label3.place(x=50, y=160)

label4 = Label(m, text='Wind Speed', font=('Helvetica',11),fg='white', bg='#203243')
label4.place(x=50, y=180)

label5 = Label(m, text='Description', font=('Helvetica',11),fg='white', bg='#203243')
label5.place(x=50, y=200)

search_image = PhotoImage(file="Images/Rounded Rectangle 3.png")
myimage = Label(m, image=search_image,bg='#57adff')
myimage.place(x=270, y=120)

cloud_image = PhotoImage(file='Images/Layer 7.png')
weather_image = Label(m, image=cloud_image,bg='#203243')
weather_image.place(x=290, y=127)

text_field = tk.Entry(m, justify='center',width=15,font=('poppins',25,'bold'), bg='#203243',fg='white',border=0)
text_field.place(x=370,y=130)
text_field.focus()

search_icon = PhotoImage(file='Images/Layer 6.png')
icon_image = Button(image=search_icon,borderwidth=0,bg='#203243')
icon_image.place(x=645,y=125)

frame = Frame(m, width=900, height=180, bg='#212120')
frame.pack(side=BOTTOM)

first_box = PhotoImage(file='Images/Rounded Rectangle 2.png')
second_box = PhotoImage(file='Images/Rounded Rectangle 2 copy.png')

Label(frame, image=first_box, bg='#212120').place(x=30,y=20)
Label(frame, image=second_box, bg='#212120').place(x=300,y=30)
Label(frame, image=second_box, bg='#212120').place(x=400,y=30)
Label(frame, image=second_box, bg='#212120').place(x=500,y=30)
Label(frame, image=second_box, bg='#212120').place(x=600,y=30)
Label(frame, image=second_box, bg='#212120').place(x=700,y=30)
Label(frame, image=second_box, bg='#212120').place(x=800,y=30)
m.mainloop()