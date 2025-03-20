########################################################################
# author: Rylie Malbrough
# date: 10/26/2022
# description: Logbook
########################################################################

# A function that prompts the user for the minimum value and returns it
# to the calling statement. Function to also deal with range checking to
# make sure that minimum value provided is greater than 0

import math 

def getMinimum():
    min = float(input("What is the minimum value? ")) #type as float so it accepts both float and int

    if (min < 0) or (min == 0): 
        print("ERROR: Minimum value should be greater than 0")
        getMinimum()     #call function again
    else:
        return round(min,4) #round to four decimal places

  
# A function that prompts the user for the maximum value and returns it
# to the calling statement. Function receives argument that is used in
# range checking to make sure maximum value provided by user is greater
# than minimum value (provided in function argument)

def getMaximum():
    max = float(input("What is the maximum value? "))
        
    if (max < 0) or (max == 0):
        print("ERROR: Maximum value should be greater than 0")
        getMaximum()
    else:
        return round(max,4)
        

# A function that prompts the user for the step size and returns it to
# the calling statement. Function also deals with range checking to make
# sure that step size provided is greater than 0.

def getStep():
    step = float(input("What is the step size? "))

    if (step < 0) or (step == 0):
        print("ERROR: Step size should be greater than 0")
        getStep()
    else:
        return round(step, 4) 

# A function that receives a number as an argument and returns the log
# of that number rounded to 4 decimal places.

def logarithm(number):

    answer = math.log(number, 10)
    return round(float(answer), 4)

# A function that receives the value at the left size of the log table
# (i.e. the value whose logarithms should be calculated). The function
# then creates a row of logarithmic values for that argument counting
# upwards in steps of 1 significant figure more than the argument. i.e.
# if the argument is 1.3, then the row gives values of the logs for
# 1.30, 1.31, 1.32, 1.33, ..., 1.39. If the argument is 2.456, then it
# gives logs for 2.4560, 2.4561, 2.4562, 2.4563, ..., 2.4569

def getRows(first_element):
        

    if first_element.is_integer() == True:      #if parameter is an integer
 
        count = -1
        list = [];      

        if count == -1:
            list.append(str(float(first_element)) + "\t")   #need to print out the initial value
            count = 0                                       #need to start at 0 so it takes the log of the initial value
            
        while count < .9:                           #since it's an integer, I can add numbers to it (perform operations)
            element = first_element + count
            log = logarithm(float(element))         #taking log of my integer + count
            list.append(str(log) + "\t")            #add the log to the list
            count = count + .1

        print(*list)    #print list in one line
       
        
    if first_element.is_integer() == False:         #if parameter is not an integer 

        count = -1
        list2 = [];

        if count == -1:
            list2.append(str(first_element) + "\t")
            count = 0

        while count < 9:        
            element = str(first_element) + str(count)           #concatonate number to the end of the value
            log = logarithm(float(element))
            list2.append(str(log) + "\t")
            count = count + 1

        print(*list2)
        
        
# A function that receives the minimum, maximum and step size as
# arguments, and prints the table (making use of the function that
# creates a single row defined earlier)

def getTable(maximum, minimum, stepSize):

    print( "\t" + "0"  + "\t"  + "1"  + "\t" + "2"  + "\t" + "3"
           + "\t" + "4" + "\t" + "5" + "\t" + "6"  + "\t" + "7" + "\t"          #I also agree that this is a terrible way of doing it. . . I had no choice I swear
           + "8"  + "\t" + "9")

    print("------------------------------------------------------------------------------------------")
    
    count = minimum           #declaring variable for minimum
    x = 1                     #initialize x as one
    
    while count < maximum:    #yes
        
        getRows(count)        #call function for initial value (minimum)
        count = minimum + stepSize*x         #update variable by adding the stepSize to minimum
        x = x + 1             #update x so that the stepSize grows

####################### MAIN #########################################
# Get the minimum, maximum and step size from the user using functions
# defined earlier.

minimum = getMinimum()
maximum = getMaximum()
stepSize = getStep()

# create the table using the function defined eariler.

getTable(maximum, minimum, stepSize)



