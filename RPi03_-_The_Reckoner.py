###################################################################
# Name: Rylie Malbrough                                           #
# Date: 2/1/2023                                                  #                  
# Description: The Reckoner                                       #
###################################################################
from tkinter import *
from time import *

#the main GUI
class MainGUI(Frame):
 
    def __init__(self, parent):                                     #constructor
        Frame.__init__(self, parent, bg="white")
        self.setupGUI()

    #sets up the GUI
    def setupGUI(self):
        #setting up display
        self.display = Label(self, text=" ", anchor=E, bg="white", height=1,font=("TexGyreAdventor", 45))

        #putting display on top row, expanding it to all four sides
        self.display.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S)

        #configure rows and columns to adjust to the window, there are 6 rows
        for row in range(6):
            Grid.rowconfigure(self, row, weight=1)

        #there are four columns(0,3)
        for col in range(4):
            Grid.columnconfigure(self, col, weight=1)
            
        #############    
        #FIRST ROW  #
        #############
            
        ####### ( button#######
        #get the image
        img = PhotoImage(file="lpr.gif")
        #create button
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness = 0, activebackground="white", command=lambda:self.process("("))
        #set button's img
        button.image = img
        #align button
        button.grid(row=1, column=0, sticky=N+S+E+W)
        
        ####### ) button######
        img = PhotoImage(file="rpr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process(")"))
        button.image = img
        button.grid(row=1, column=1, sticky=N+S+E+W)

        ########AC button#####
        img = PhotoImage(file="clr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("AC"))
        button.image = img
        button.grid(row=1, column=2, sticky=N+S+E+W)

        #####Back space#####
        img = PhotoImage(file="bak.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("del"))
        button.image = img
        button.grid(row=1, column=3, sticky=N+S+E+W)

        ##############
        # SECOND ROW #
        ##############
        
        ######seven######
        img = PhotoImage(file="7.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("7"))
        button.image = img
        button.grid(row=2, column=0, sticky=N+S+E+W)

        #####eight#######
        img = PhotoImage(file="8.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("8"))
        button.image = img
        button.grid(row=2, column=1, sticky=N+S+E+W)

        ######nine#######
        img= PhotoImage(file="9.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("9"))
        button.image = img
        button.grid(row=2, column=2, sticky=N+S+E+W)

        #####division####
        img = PhotoImage(file="div.gif")
        button=Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("/"))
        button.image=img
        button.grid(row=2, column=3, sticky=N+S+E+W)

        #################
        # THIRD ROW     #
        #################

        ######four#######
        img = PhotoImage(file="4.gif")
        button=Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,activebackground="white", command=lambda:self.process("4"))
        button.image=img
        button.grid(row=3, column=0, sticky=N+S+E+W)

        ######five#######
        img = PhotoImage(file="5.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("5"))
        button.image = img
        button.grid(row=3,column=1, sticky=N+S+E+W)

        ######six########
        img = PhotoImage(file="6.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("6"))
        button.image=img
        button.grid(row=3, column=2, sticky=N+S+E+W)

        ##multiplication##
        img = PhotoImage(file="mul.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("*"))
        button.image=img
        button.grid(row=3, column=3, sticky=N+S+E+W)

        #################
        # FOURTH ROW    #
        #################

        ######one#######
        img = PhotoImage(file="1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("1"))
        button.image=img
        button.grid(row=4, column=0, sticky=N+S+E+W)

        ######two#######
        img = PhotoImage(file="2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("2"))
        button.image=img
        button.grid(row=4, column=1, sticky=N+S+E+W)

        ####three#######
        img = PhotoImage(file="3.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("3"))
        button.image=img
        button.grid(row=4, column=2, sticky=N+S+E+W)

        ###subtraction##
        img = PhotoImage(file="sub.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("-"))
        button.image=img
        button.grid(row=4, column=3, sticky=N+S+E+W)

        #################
        #   FIFTH ROW   #
        #################

        #####zero#######
        img = PhotoImage(file="0.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("0"))
        button.image=img
        button.grid(row=5, column=0, sticky=N+S+E+W)

        ######dot#######
        img = PhotoImage(file="dot.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("."))
        button.image=img
        button.grid(row=5, column=1, sticky=N+S+E+W)

        ####addition###
        img = PhotoImage(file="add.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("+"))
        button.image=img
        button.grid(row=5, column=3, sticky=N+S+E+W)

        ###############
        #  SIXTH ROW  #
        ###############
        
        #####equal######
        img = PhotoImage(file="eql-wide.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("="))
        button.image=img
        button.grid(row=6, column=0, columnspan=2, sticky=W)
        
        #####modulus###
        img = PhotoImage(file="mod.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("%"))
        button.image=img
        button.grid(row=6, column=2, sticky=N+S+E+W)

        ######Power button####
        img = PhotoImage(file="pow.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda:self.process("**"))
        button.image = img
        button.grid(row=6, column=3, sticky=N+S+E+W)
        
        #PACK GUI
        self.pack(fill=BOTH, expand=1)

    #processes button presses
   
    def process(self,button):
        
        if(button=="AC"):                  #AC clears display
            self.display["text"] = " "       #clear display

        elif(button=="="):                   # = starts evaluation
            expr = self.display["text"]      #display evaluation, may return an error   
            try:
                result=eval(expr)                    #evaluate expression
                self.display["text"] = str(result)   #store result in display
                answer = str(result)
                if len(answer) >= 14:                #if length of string is longer than 14
                    answer = answer[0:11] + "..."    #truncate and add ...
                    self.display["text"] = answer
            except:
                self.display["text"] = 'ERROR'                #error on display if error occurs
                sleep(2)                                      #wait  
                self.process["AC"]                            #clear
                
        elif(button=="del"):
            display = self.display["text"]          #set variable equal to display text
            last = int(len(str(display))-1)         #get last value in index
            new = display[0: last]                  #change index of display to disclude last index
            self.display["text"] = new              #change to new display
            
        elif len(self.display["text"]) == 14:               #if the display is 14 digits
             self.display["text"] = self.display["text"]    #just keep at 14 digits     
        else:
            self.display["text"] += button     #concatonate button value to text

    
        

    
################################main###############################
#Create the window

window = Tk()

#Set the window title

window.title("The Reckoner")

#Generate the GUI

p = MainGUI(window)

#display the GUI and wait for user interaction

window.mainloop()
