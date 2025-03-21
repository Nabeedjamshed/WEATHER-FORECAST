from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
import pyodbc
m = Tk()
m.title("Weather App")
m.geometry('890x470+300+200')
m.configure(bg='#3f92ff')
m.resizable(False, False)



def history():
    new = Toplevel()
    new.title("History")
    new.configure(bg='#2c3e50')
    screen_width = new.winfo_screenwidth()
    screen_height = new.winfo_screenheight()
    new.geometry(f"{screen_width}x{screen_height}+0+0")

    icon = PhotoImage(file="Images/logo.png")
    new.iconphoto(True,icon)
    l1 = Label(new, text="Weather Forecast History", font=('Arial', 40), bg='black', fg='white', width=10, height=1)
    l1.pack(side=TOP, fill=X)
    
    right_cloud1 = (Image.open('Images/black1.webp'))
    new1 = right_cloud1.resize((150, 60))
    b_cloud1 = ImageTk.PhotoImage(new1)
    
    img1 = Label(new, image=b_cloud1, bg='black')
    img1.image=b_cloud1
    img1.place(x=2, y=1)
    

    right_cloud2 = Image.open('Images/black2.webp')
    new2 = right_cloud2.resize((150, 60))
    b_cloud2 = ImageTk.PhotoImage(new2)

    img2 = tk.Label(new, image=b_cloud2, bg='black')
    img2.place(x=1200, y=1)

    cor1 = Image.open('Images/corner1.jpeg')
    new3 = cor1.resize((150, 203))
    c_1 = ImageTk.PhotoImage(new3)

    f_image = Label(new, image=c_1, bg='#2c3e50')
    f_image.place(x=0, y=67)

    cor2 = Image.open('Images/corner2.jpeg')
    new4 = cor2.resize((150, 203))
    c_2 = ImageTk.PhotoImage(new4)

    s_image = Label(new, image=c_2, bg='#2c3e50')
    s_image.place(x=1206, y=65)

    water1 = Image.open('Images/w1.webp')
    new5 = water1.resize((160, 230))  
    w_1 = ImageTk.PhotoImage(new5)

    t_image = Label(new, image=w_1, bg='#2c3e50')  
    t_image.place(x=1200, y=490)

    wind1 = Image.open('Images/wind.jpeg')
    new6 = wind1.resize((150, 250))  
    wind_1 = ImageTk.PhotoImage(new6)

    fr_image = Label(new, image=wind_1, bg='#2c3e50')
    fr_image.place(x=0, y=490)

    fi_frame = Frame(new, width=1046, height=300, bg='black')
    fi_frame.place(x=155, y=668)

    six_frame = Frame(new,width=37, height=218, bg='black')
    six_frame.place(x=0,y=272)

    sev_frame = Frame(new,width=37, height=220, bg='black')
    sev_frame.place(x=1322,y=270)
    connector=r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\workspace\weather-forecast\weather_app.accdb'
    connection=pyodbc.connect(connector)
    cursor=connection.cursor()
    cursor.execute("SELECT TOP 7 Location,temp,c_time FROM PL_Project ORDER BY index DESC  ")
    row=cursor.fetchall() 
    style=ttk.Style()
    style.configure('Treeview.Heading',font=("Arial black",14,"bold"))
    tree_view=ttk.Treeview(new) 
    tree_view.tag_configure('font',font=('Arial',12))
    tree_view.tag_configure('bg', background="light blue")
    tree_view['columns']=('Location','Temperature','Time')
    tree_view.heading('Location',text="LOCATION",anchor=W)
    tree_view.heading('Temperature',text="TEMP(°C)",anchor=W)
    tree_view.heading('Time',text="TIME",anchor=W)



    for i in row:
        tree_view.insert('',index='end',values=(i[0],i[1],i[2]),tags=('font','bg'))  
    tree_view.pack(padx=50,pady=200)

    new.mainloop()

def getweather():
    try:
        Result = Label(m,bg='#3f92ff',width=32,height=2)
        Result.place(x=390, y=190)
        city = textfield.get()
        geolocator = Nominatim(user_agent="Weather_App")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()

        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        timezone.config(text=result)
        long_lat.config(text=f'{round(location.latitude), 4}°N, {round(location.longitude), 4}°E')

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = str(local_time.strftime('%I:%M %p'))
        
        clock.config(text=current_time)
        #API connection:
        api = r"https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&appid=ad6e4ad799bcb26d267de424771618f3"
        json_data = requests.get(api).json()
        history_api=r'https://api.openweathermap.org/data/2.5/forecast?lat='+str(location.latitude)+"&lon="+str(location.longitude)+'&appid=ad6e4ad799bcb26d267de424771618f3'
        json_data_2=requests.get(history_api).json()
        temp = json_data['main']['temp']
        in_celcius=str(temp-273)[:2]
        humidity = json_data['main']['humidity']
        pressure = json_data['main']['pressure']
        wind = json_data['wind']['speed']
        description = json_data['weather'][0]['description']
        t.config(text=(in_celcius,'°C'))
        h.config(text=(humidity,'%'))
        p.config(text=(pressure,'hPa'))
        w.config(text=(wind,'m/s'))
        d.config(text=description)
        connector=r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\workspace\weather-forecast\weather_app.accdb'
        connection=pyodbc.connect(connector)
        cursor=connection.cursor()
        cursor.execute(f"INSERT INTO PL_Project (Location,temp,c_time) VALUES ('{city}','{in_celcius}','{current_time}')")
        cursor.commit()
        tempday1 = json_data['main']['temp_max']
        tempnight = json_data['main']['temp_min']
        img = (Image.open('project pics/icon/02n@2x.png'))
        photo1 = ImageTk.PhotoImage(img)
        firstimage.config(image=photo1)
        firstimage.image=photo1
        in_celcius1=tempday1-273
        in_celcius2=tempnight-273
        day1temp.config(text=f"Day:{round(in_celcius1,2)}\n  Night:{round(in_celcius2,2)}")
        
        img = (Image.open('project pics/icon/02d@2x.png'))
        resized_image = img.resize((50,50))
        photo2 = ImageTk.PhotoImage(resized_image)
        secondimage.config(image=photo2)
        secondimage.image=photo2
        tempday2 = json_data_2['list'][8]['main']['temp_max']
        tempnight = json_data_2['list'][15]['main']['temp_min']
        in_celcius1=tempday2-273
        in_celcius2=tempnight-273
        day2temp.config(text=f"Day:{round(in_celcius1,2)}\n  Night:{round(in_celcius2,2)}")

        img = (Image.open('project pics/icon/02d@2x.png'))
        resized_image = img.resize((50,50))
        photo2 = ImageTk.PhotoImage(resized_image)
        thirdimage.config(image=photo2)
        thirdimage.image=photo2
        tempday3 = json_data_2['list'][11]['main']['temp_max']
        tempnight = json_data_2['list'][18]['main']['temp_min']
        in_celcius1=tempday3-273
        in_celcius2=tempnight-273
        day3temp.config(text=f"Day:{round(in_celcius1,2)}\n  Night:{round(in_celcius2,2)}")

        img = (Image.open('project pics/icon/02d@2x.png'))
        resized_image = img.resize((50,50))
        photo2 = ImageTk.PhotoImage(resized_image)
        fourthimage.config(image=photo2)
        fourthimage.image=photo2
        tempday4 = json_data_2['list'][19]['main']['temp_max']
        tempnight = json_data_2['list'][26]['main']['temp_min']
        in_celcius1=tempday4-273
        in_celcius2=tempnight-273
        day4temp.config(text=f"Day:{round(in_celcius1,2)}\n  Night:{round(in_celcius2,2)}")

        img = (Image.open('project pics/icon/02d@2x.png'))
        resized_image = img.resize((50,50))
        photo2 = ImageTk.PhotoImage(resized_image)
        fifthimage.config(image=photo2)
        fifthimage.image=photo2
        tempday5 = json_data_2['list'][27]['main']['temp_max']
        tempnight = json_data_2['list'][34]['main']['temp_min']
        in_celcius1=tempday5-273
        in_celcius2=tempnight-273
        day5temp.config(text=f"Day:{round(in_celcius1,2)}\n  Night:{round(in_celcius2,2)}")

        img = (Image.open('project pics/icon/02d@2x.png'))
        resized_image = img.resize((50,50))
        photo2 = ImageTk.PhotoImage(resized_image)
        sixthimage.config(image=photo2)
        sixthimage.image=photo2
        tempday6 = json_data_2['list'][31]['main']['temp_max']
        tempnight = json_data_2['list'][38]['main']['temp_min']
        in_celcius1=tempday6-273
        in_celcius2=tempnight-273
        day6temp.config(text=f"Day:{round(in_celcius1,2)}\n  Night:{round(in_celcius2,2)}")

        img = (Image.open('project pics/icon/02d@2x.png'))
        resized_image = img.resize((50,50))
        photo2 = ImageTk.PhotoImage(resized_image)
        seventhimage.config(image=photo2)
        seventhimage.image=photo2
        tempday7 = json_data_2['list'][35]['main']['temp_max']
        tempnight = json_data_2['list'][35]['main']['temp_min']
        in_celcius1=tempday7-273
        in_celcius2=tempnight-273
        day7temp.config(text=f"Day:{round(in_celcius1,2)}\n  Night:{round(in_celcius2,2)}")
        
        first = datetime.now()
        day1.config(text=first.strftime("%A"))

        second = first+timedelta(days=1)
        day2.config(text=second.strftime("%A"))

        third = first+timedelta(days=2)
        day3.config(text=third.strftime("%A"))

        fourth = first+timedelta(days=3)
        day4.config(text=fourth.strftime("%A"))

        fifth = first+timedelta(days=4)
        day5.config(text=fifth.strftime("%A"))

        sixth = first+timedelta(days=5)
        day6.config(text=sixth.strftime("%A"))

        seventh = first+timedelta(days=6)
        day7.config(text=seventh.strftime("%A"))
    except:
        messagebox.showerror("Error","Invalid Location!")
    
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

# Load images
search_image = tk.PhotoImage(file="Images/Rounded Rectangle 3.png")
cloud_image = tk.PhotoImage(file='Images/Layer 7.png')
search_icon = tk.PhotoImage(file='Images/Layer 6.png')

# Create and place labels
myimage = tk.Label(m, image=search_image, bg='#3f92ff')
myimage.place(x=270, y=120)

weather_image = tk.Label(m, image=cloud_image, bg='#203243')
weather_image.place(x=290, y=127)

# Create and place entry widget
textfield = tk.Entry(m, justify='center', width=15, font=('poppins', 25, 'bold'), bg='#203243', border=0, fg='white')
textfield.place(x=370, y=130)
textfield.focus()

# Create and place button with the search icon
search_button = tk.Button(m, image=search_icon, borderwidth=0, cursor='hand2', bg='#203243',command=getweather)
search_button.place(x=645, y=125)
history_data=Button(m,text="Histroy",command=history)
history_data.place(x=830,y=250)
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

#clock (here we place a time)
clock = Label(m, font=('Helvetica', 30, 'bold'), fg='white', bg='#3f92ff')
clock.place(x=30, y=20)

timezone = Label(m, font=('Helvetica', 20), fg='white', bg='#3f92ff')
timezone.place(x=680, y=20)

long_lat = Label(m, font=('Helvetica', 10), fg='white', bg='#3f92ff')
long_lat.place(x=680, y=60)

t = Label(m, font=('Helvetica', 11), fg='white', bg='#203243')
t.place(x=145, y=120)

h = Label(m, font=('Helvetica', 11), fg='white', bg='#203243')
h.place(x=145, y=140)

p = Label(m, font=('Helvetica', 11), fg='white', bg='#203243')
p.place(x=145, y=160)

w = Label(m, font=('Helvetica', 11), fg='white', bg='#203243')
w.place(x=145, y=180)

d = Label(m, font=('Helvetica', 11), fg='white', bg='#203243')
d.place(x=145, y=200)

firstframe = Frame(m, width=230, height=132, bg='#282829')
firstframe.place(x=35, y=315)

day1 = Label(firstframe,font="arial 20", bg='#282829', fg='#fff')
day1.place(x=100,y=5)

firstimage = Label(firstframe,bg='#282829')
firstimage.place(x=1, y=15)

day1temp =Label(firstframe,bg='#282829',fg='#57adff',font=('arial',15,'bold'))
day1temp.place(x=100,y=50)

secondframe = Frame(m, width=70, height=115, bg='#282829')
secondframe.place(x=305, y=325)

day2 = Label(secondframe, bg='#282829', fg='#fff')
day2.place(x=6,y=5)

secondimage = Label(secondframe,bg='#282829')
secondimage.place(x=7, y=20)

day2temp = Label(secondframe,bg='#282829',fg='#fff')
day2temp.place(x=0,y=70)

thirdframe = Frame(m, width=70, height=115, bg='#282829')
thirdframe.place(x=405, y=325)

day3 = Label(thirdframe, bg='#282829', fg='#fff')
day3.place(x=6,y=5)

thirdimage = Label(thirdframe,bg='#282829')
thirdimage.place(x=7, y=20)

day3temp = Label(thirdframe,bg='#282829',fg='#fff')
day3temp.place(x=0,y=70)

fourthframe = Frame(m, width=70, height=115, bg='#282829')
fourthframe.place(x=505, y=325)

day4 = Label(fourthframe, bg='#282829', fg='#fff')
day4.place(x=6,y=5)

fourthimage = Label(fourthframe,bg='#282829')
fourthimage.place(x=7, y=20)

day4temp = Label(fourthframe,bg='#282829',fg='#fff')
day4temp.place(x=0,y=70)

fifthframe = Frame(m, width=70, height=115, bg='#282829')
fifthframe.place(x=605, y=325)

day5 = Label(fifthframe, bg='#282829', fg='#fff')
day5.place(x=6,y=5)

fifthimage = Label(fifthframe,bg='#282829')
fifthimage.place(x=7, y=20)

day5temp = Label(fifthframe,bg='#282829',fg='#fff')
day5temp.place(x=0,y=70)

sixthframe = Frame(m, width=70, height=115, bg='#282829')
sixthframe.place(x=705, y=325)

day6 = Label(sixthframe, bg='#282829', fg='#fff')
day6.place(x=6,y=5)

sixthimage = Label(sixthframe,bg='#282829')
sixthimage.place(x=7, y=20)

day6temp = Label(sixthframe,bg='#282829',fg='#fff')
day6temp.place(x=0,y=70)

seventhframe = Frame(m, width=70, height=115, bg='#282829')
seventhframe.place(x=805, y=325)

day7 = Label(seventhframe, bg='#282829', fg='#fff')
day7.place(x=6,y=5)

seventhimage = Label(seventhframe,bg='#282829')
seventhimage.place(x=7, y=20)

day7temp = Label(seventhframe,bg='#282829',fg='#fff')
day7temp.place(x=0,y=70)

m.mainloop()