import serial
import time
from tkinter import *
from tkinter import font
import customtkinter

global currentScreen
currentScreen = 1

#arduino = serial.Serial(port='COM3', baudrate=9600)


##############################TKINTER#########################################################
# Configure window
window = customtkinter.CTk()
window.title("Enclosure Settings")
window.geometry=("1000x600")
customtkinter.set_appearance_mode("Light")

# Setting up Frames 
ScreenOne = customtkinter.CTkFrame(window, width=500, height=500)        
ScreenTwo = customtkinter.CTkFrame(window, width=500, height=500)   
ScreenThree = customtkinter.CTkFrame(window, width=500, height=500)
ScreenFour = customtkinter.CTkFrame(window, width=500, height=500)
ScreenFive = customtkinter.CTkFrame(window, width=500, height=500)
ScreenSix = customtkinter.CTkFrame(window, width=500, height=500)

# Set mode to light mode so that colors appear lighter
customtkinter.set_appearance_mode("light mode")

###############FONTS#############################

font1 = customtkinter.CTkFont(family = "Lexend", size = 25)
font2 = customtkinter.CTkFont(family="Lexend", size=50)
font3 = customtkinter.CTkFont(family="Calibri", size=50, underline=True)
font4 = customtkinter.CTkFont(family="Calibri", size=18)

################Screen One#######################
def switchScreen2():
    currentScreen = 2
    ScreenTwo.pack()                                #load screen two 
    ScreenOne.pack_forget()                         #forget screen one
    
def switchScreen3():
    ScreenThree.pack()                              #load screen two 
    ScreenOne.pack_forget()                         #forget screen one
    currentScreen = 3

# Details button
button = customtkinter.CTkButton(ScreenOne,font=font1, fg_color=("green"),  width=200, height=50, text="Details",command=switchScreen2)
button.grid(column=0, row=2, pady=20, padx=200)

# Options button
button2 = customtkinter.CTkButton(ScreenOne,font=font1,fg_color=("green"), width=200, height=50, text="Options",command=switchScreen3)
button2.grid(column=0, row=3, pady=20, padx=200)

# Lizard Image
img = PhotoImage(file="lizard.png")
label = customtkinter.CTkLabel(ScreenOne,text="", image = img)
label.grid(column=0, row=0, padx=10, pady=10)

ScreenOne.pack()

################Screen Two########################
def switchScreen1():
    ScreenOne.pack()
    ScreenTwo.pack_forget()

# Gets temperature from Arduino string
'''
def getTemp():
    temperature = arduino.readline()
    temperature = temperature.decode()
    return str(temperature)[3:5]

# Gets humidity from Arduino string
def getHumid():
    humidity = arduino.readline()
    humidity = humidity.decode()
    return str(humidity)[0:3] + "%"

def updateTemp():
    ScreenTwo.pack_forget()
    ScreenOne.pack()
    '''

# Return Button  
button3 = customtkinter.CTkButton(ScreenTwo, width=100, fg_color=("green"), height=30, text="Return",command=switchScreen1)
button3.grid(column=0, row=10, padx=200, pady=500, sticky=S)

#######TEMPERATURE######
# Title for Temperature
label = customtkinter.CTkLabel(ScreenTwo, text="Temperature", height=70, anchor=CENTER, font=font3)
label.grid(column=0, row=0, pady=20)

# Image for Temperature
img2 = PhotoImage(file="temperature.png")
label2 = customtkinter.CTkLabel(ScreenTwo, text="", image = img2)
label2.place(relx = 0.24, rely = 0.27, anchor=CENTER)

# Temperature value
label3 = customtkinter.CTkLabel(ScreenTwo,font=font2, anchor=E, text="87°F")
label3.place(relx = 0.50, rely=0.256, anchor = CENTER)

#######HUMIDITY########
# Title for Humidity
label4 = customtkinter.CTkLabel(ScreenTwo, text="Humidity", height=70, anchor=CENTER, font=font3)
label4.place(relx = 0.5, rely=0.50, anchor=CENTER)

# Image for humidity
img3 = PhotoImage(file="humidity.png")
label5 = customtkinter.CTkLabel(ScreenTwo, text="", image=img3)
label5.place(relx=0.25, rely=0.67, anchor=CENTER)

# Humidity values
label6 = customtkinter.CTkLabel(ScreenTwo,font=font2, anchor=E, text="56%")
label6.place(relx = 0.52, rely=0.67, anchor = CENTER)

################Screen Three########################
def switchScreen1():
    ScreenOne.pack()
    ScreenThree.pack_forget()
    currentScreen = 1

def switchScreen4():
    ScreenFour.pack()
    ScreenThree.pack_forget()
    currentScreen = 4

def switchScreen5():
    ScreenFive.pack()
    ScreenThree.pack_forget()
    currentScreen = 5

def switchScreen6():
    ScreenSix.pack()
    ScreenThree.pack_forget()
    currentScreen = 6

# Return Button
button4 = customtkinter.CTkButton(ScreenThree, fg_color=("green"), width=100, height=30, text="Return",command=switchScreen1)
button4.grid(column=0, row=10, padx=200, pady=500, sticky=S)

# Title
label = customtkinter.CTkLabel(ScreenThree, text="Choose your lizard:", height=100, anchor=CENTER, font=font3)
label.grid(column=0, row=1, padx=10, pady=10)

# Bearded Dragon Button
button = customtkinter.CTkButton(ScreenThree,font=font1, fg_color=("green"),  width=200, height=50, text="Bearded Dragon",command=switchScreen4)
button.grid(column=0, row=2, pady=20, padx=200)

# Crested Gecko Button
button = customtkinter.CTkButton(ScreenThree,font=font1, fg_color=("green"),  width=200, height=50, text="Crested Gecko",command=switchScreen5)
button.grid(column=0, row=3, pady=20, padx=200)

# Leopard Gecko Button
button = customtkinter.CTkButton(ScreenThree,font=font1, fg_color=("green"),  width=200, height=50, text="Leopard Gecko",command=switchScreen6)
button.grid(column=0, row=4, pady=20, padx=200)

################Screen Four########################################
# Displays information about Bearded Dragons

def switchScreen1():
    ScreenOne.pack()
    ScreenFour.pack_forget()

# Return button
button = customtkinter.CTkButton(ScreenFour, width=100, fg_color=("green"), height=30, text="Return", command=switchScreen1)
button.place(rely=0.8, relx=0.4)

# Bearded dragon image
img3 = PhotoImage(file="bearded dragon.png")
label = customtkinter.CTkLabel(ScreenFour, text='', image = img3)
label.place(relx=0.5, rely=0.2, anchor=CENTER)

# Description
label = customtkinter.CTkLabel(ScreenFour, font=font4, bg_color="white", text="During the day, bearded dragons need\n a basking area with a temperature of\n 104-107°F. They should also have a cool\n end of the enclosure around 71-77°F.\n They require around 35-40% humidity in\n the enclosure. Hit the update button to\n set the humidity for your pet. ")
label.place(relx=0.21, rely=0.42)

##############Screen Five###########################################
# Displays information on crested geckos

def switchScreen1():
    ScreenOne.pack()
    ScreenFive.pack_forget()

# Return button 
button = customtkinter.CTkButton(ScreenFive, width=100, fg_color=("green"), height=30, text="Return", command=switchScreen1)
button.place(rely=0.8, relx=0.4)

# Crested gecko image
img4 = PhotoImage(file="crested gecko.png")
label = customtkinter.CTkLabel(ScreenFive, text='', image=img4)
label.place(relx=0.5, rely=0.2, anchor=CENTER)

# Crested gecko description
label = customtkinter.CTkLabel(ScreenFive,bg_color="white", font=font4, text="  Crested geckos are sensitive to high\n  temperatures, so the cage shouldn't be\n  be kept above 80°F. The temperature\n  should be kept around 72-75°F. Humidity\n   should kept around 60-80%, but\n  overdoing it may cause mold. Hit the\n   update button to set the humidity for your pet.  " )
label.place(relx=0.16, rely=0.42)


###############Screen Six############################################
# Displays information on leopard geckos

def switchScreen1():
    ScreenOne.pack()
    ScreenSix.pack_forget()
    
# Return button 
button = customtkinter.CTkButton(ScreenSix, width=100, fg_color=("green"), height=30, text="Return",command=switchScreen1)
button.place(rely=0.8, relx=0.4)

# Leopard gecko image
img5 = PhotoImage(file="leopard gecko.png")
label = customtkinter.CTkLabel(ScreenSix, text='', image=img5)
label.place(relx=0.5, rely=0.2, anchor=CENTER)

# Leopard gecko description
label = customtkinter.CTkLabel(ScreenSix, bg_color="white", font=font4, text="Ideal temperatures Leopard Geckos \n range from 75-80°F on the cool side \n and 80-85°F on the warm side. Provide \n a 90-95°F basking area on \n the warm side. Humidity \n should be kept at 30-40%. Hit \n the update button to set the \n humidity for your pet.")
label.place(relx=0.20, rely=0.38)

# Loop window
window.mainloop()

