#################################################################################
# Name: Rylie Malbrough                                                         #                
# Date: 1/27/2023                                                               #         
# Description: My Binary Addiction                                              #                   
#################################################################################

import RPi.GPIO as GPIO                         #bring in GPIO functionality
from time import sleep                          #sleep
from random import randint                      #generates random integers

#function that defines the GPIO pins for the nine output LEDS
def setGPIO():
    #define the pins
    gpio = [17, 18, 27, 22, 26, 12, 16, 20, 21]
    #set them up as output pins
    GPIO.setup(gpio, GPIO.OUT)
    
    return gpio

#function that randomly generates an 8-bit binary number
def setNum():
    #create an empty list to represent the bits
    num = []
    #generate the eight random bits
    for i in range(0,8):
        #append a random bit(0 or 1) to the end of the list
        num.append(randint(0,1))

    return num

def display():
    for i in range(len(sum)):
        #if the i-th bit is 1, then turn the i-th LED on
        if (sum[i] == 1):
            GPIO.output(gpio[i], GPIO.HIGH)
        #otherwise, turn it off
        else:
            GPIO.output(gpio[i], GPIO.LOW)

def fullAdder(Cin, A, B):
    S1 = (~A & B) ^ (~B & A)                #get first sum, "not A and B" or "not B and A
    C = A & B                               #get carry, A and B
    S2 = (~S1 & Cin) ^ (S1 & ~Cin)          #Get second sum from the Cin
    C2 = Cin & S1                           #get carry
    Cout = C2 ^ C                           #get second carry

    return S2, Cout

def calculate(num1, num2):
    Cout = 0                    #initial cout is zero
    sum = []                    #initialize the sum
    n = len(num1) - 1           #position of the right-most bit of num1

#step through each bit, from right to left
    while (n >= 0):
        #isolate A and B (the current bits of num1 and num2)
        A = num1[n]
        B = num2[n]
        #set the Cin (as the previous half adder's Cout)
        Cin = Cout

        #call the fulLAdder function that takes Cin, A,
        #and B, nd returns S and Cout
        S2, Cout = fullAdder(Cin, A, B)

        #insert sum bit, S at the beginning (index 0) of sum
        sum.insert(0, S2)

        #go to next bit position (to the left)
        n -= 1
        
    #insert final carry out at the beginning of the sum
    sum.insert(0, Cout)

    return sum

#################################main######################################
#use the broadcom pin scheme
GPIO.setmode(GPIO.BCM)

#setup the GPIO pins
gpio = setGPIO()

#get a random num1 and display it to the console
num1 = setNum()
print("     ", num1)

#get a random num2 and display it to the console
num2 = setNum()
print ("+   ",num2)

#calculate the sum of num1 + num2 and display it to the console
sum = calculate(num1, num2)
print ("=  ", sum)

#turn on the appropriate LEDs to "display" the sum
display()

#wait for user input before cleanng up and resetting GPIO pins
input("Press ENTER to terminate")
GPIO.cleanup()
