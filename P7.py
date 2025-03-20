####################################################################
# Name: Rylie Malbrough                                            # 
# Description: Input analyzer                                      # 
# Date: 2/13/2023                                                  #
####################################################################

from tkinter import *
from tkinter import font
import enchant

##########functions#################################################
#checks to see if a number is a float############
def isFloat(number):
    try:
        float(number)           #try to turn it into float
        return True
    except:
        return False            #if it doesn't work then yeah doesn't work
    
#checks to see if a number is an integer#########
def isInt(number):
    try:
        int(number)             #try to turn it into float
        return True
    except:
        return False
#determines if a number is even or odd###########    

def even_or_odd(r):
    if r % 2 == 0:                  #if it's divisible by 2 evenly, it's even
        return "Even"
    else:                           #if it's not divisble by 2 evenly, it's odd
        return "Odd"
#determines if a number is prime or not#############
    
def primeNum(x):                #You can find out if a number is prime by dividing it by the numbers 2 through the square root of itself
    i = 2
    sqrt = x ** 0.5             #Finding square root x^1/2 = sqrt(x)
    while (i <= sqrt):          #Here, I'm using a while loop to repeatly divide x by i
        x / i
        if x % i == 0:          #If at any point x divides evenly into i, then return "False" (it is NOT a prime number)
            return "Not Prime"
        else:                   #Otherwise, increase i by one
            i += 1
    return "Prime"              #Once the while loop is finished and a return value was NOT given, return "True" (it IS a prime number)


#determines if a word is a valid english word#######
def checkWord(word):
    str(word)
    dictionary = enchant.Dict("en_US")      #get US dictionary
    boolean = dictionary.check(word)        #check word
    if boolean == True:                     #if it's a part of the dictionary
        return "Valid English Word"         #it's valid
    else:
        return "Not a valid English Word"   #it ain't valid

#determines close English words############
def otherWord(word):
    str(word)
    dictionary = enchant.Dict("en_US")      #get US dictionary
    boolean = dictionary.check(word)        #check word
    if boolean == True:                     #if it's a part of the dictionary
        return " "                          #no close english words
    else:
        return "Close words include: {}".format(dictionary.suggest(word))   #return close english words
    
#analyzes text to determine if it is an integer, float, or string
def analyzeType(text):
    word = text.get()                         #get text from entry
    if isFloat(word) == True:                 #check if its a float
        if isInt(word) == True:               #check if its integer
            integer = int(word)               #if it's an integer, turn it into one 
            one = "Number: " + str(integer)   #Get the number
            two = "integer"                   #print the type
            three = primeNum(integer)         #determine prime
            four = even_or_odd(integer)       #determine even or odd
            
        else:                                 #if it's not an integer, it's a float
            float1 = float(word)              #turn into float
            one = "Number: " + str(float1)    #get number
            two = "Decimal"                   #print the type
            three = primeNum(float1)          #determine prime
            four = even_or_odd(float1)        #determine even or odd
          
    else:
        string = str(word)                      #if neither float nor integer, it's string
        one = "String: " + word                 #get string
        two = "{} characters".format(len(word)) #determine characters
        three = checkWord(string)               #determine if it's valid English
        four = otherWord(string)                #get close English words (if any)
        

    return "{}\n{}\n{}\n{}".format(one,two,three,four)      #return the values
        
###############MAIN#####################
window = Tk()                       #initialize window
window.geometry("400x400")          #set pixels
window.title("Analyzer")            #set title

ScreenOne = Frame(window)           #create two frames
ScreenTwo = Frame(window)

###################FONTS#################

font1 = font.Font(family="Courier New", size="15")

##############SCREEN ONE#################
#function for switching to screen2
def switchScreen2():
    ScreenTwo.pack()                                #load screen two 
    ScreenOne.pack_forget()                         #forget screen one
    textBox2["text"] = analyzeType(textBox)         #analyze text

#entry    
textBox = Entry(ScreenOne, bg="white")
textBox.grid(column=0, row=0, columnspan=2, sticky=N+S+E+W)

#button
button = Button(ScreenOne, text="Analyze", bg="light grey", font=font1, command= switchScreen2)
button.grid(column=2, columnspan=2, row=0, sticky=N+S+E+W)

#pack
ScreenOne.pack()

##############SCREEN TWO#################
#function for switching to screen1
def switchScreen1():
    ScreenOne.pack()                #load screen one
    ScreenTwo.pack_forget()         #forget screen two 
    textBox2["text"] = " "          #clear text

#label
global textBox2
textBox2 = Label(ScreenTwo, bg="white")
textBox2.grid(column=0, row=0, columnspan=2, sticky=N+S+E+W)

#button
button = Button(ScreenTwo, text="Return", bg="light grey", font=font1, command= switchScreen1)
button.grid(column=2, columnspan=2, row=0, sticky=N+S+E+W)

##########LOOP##########################

window.mainloop()
