##########################################################################
# author: Rylie Malbrough  
# date:    12/8/2022    
# desc:   Significant Digits
#########################################################################
import random

SHOWLIST = False 	# a boolean to determine whether to show the list
MIN = 0			# the smallest random number that can be created.
MAX = 1000		# the largest random number that can be created.

# A function that prompts the user for two pieces of information i.e.
# the size of the list they want to create, and the seed that will be
# used for the list creation. It then returns both pieces of information to the
# calling statement.

def listParameters():
    size = int(input("How big a list do you want to create? "))             #getting user input for the size
    seed = int(input("What seed should be used for its creation? "))        #getting user input for the seed

    return size, seed                                                       #returning both size and seed 

# A function that prints out a list. It receives two pieces of data. The
# first is a string representing the name of the list. The second is a
# list containing all the relevant data. It proceeds to print out the
# name, and then all the elements of the data separated using a tab
# space. Both the name and the entire list are printed on a single line.

def printList(name, list):      
    print(str(name), "\t", *list)       #print out name, tab over, then print items in list

# A function that creates the list of random numbers. It receives two
# arguments: one for the size of list to be created, and another for the
# seed that will be used to create the list. The function creates the
# list using the global variables MIN and MAX to form a bound for the
# kinds of numbers that are added to the list. The list is then returned
# to the calling statement.

def randomList(size, seed):
    list = []                       #create empty list
    random.seed(seed)               #get appropriate seed from argument 

    for i in range(0, size):                   #adding numbers to the list until it reaches the total size of the list 
        list.append(random.randint(MIN, MAX))  #add random numbers from 1-1000
        i += 1                              

    return list                                #return completed list after for loop
    

# A function that recieves a list of numbers and returns another list
# containing the frequency of the lists Most Significant Digits (MSD). The
# list created by the function has 10 elements with each value
# corresponding to a different possible MSD i.e. the value in index 0
# shows the number of values in the original number list that have 0 as
# their most significant digit; the value in index 1 shows the number of
# values with 1 as their MSD; and so on and so forth. This 10 element
# list is returned to the calling statemet.

def mostSigList(list):
    numbers = []                                #create empty list 
    
    for j in range(0,10):                       #controls which number we're looking for (0-9)
        count = 0                               #number of times number appears in first digit
        for i in range(0, len(list)):           #controls index 
            element = str(list[i])              #get the appropriate element from provided index
            first_digit = int(element[0])       #get the first digit of the element
            
            if first_digit == j:                #if the digit equals the number that we're looking for (as in the MSD = 0 or 1..etc)
                count += 1                      #then increase count
                
        numbers.append(str(count) + "\t")       #once the inner for loop is done, add the count to the list and tab 

    return numbers                              #return the finished list
            
# Similar to the function above, a function that recieves a list of
# numbers, and returns another list of 10 elements where each element
# represents the frequency of a specific Least Significant Digit in the
# original list.

def leastSigList(list):
    numbers = []                                    #create empty list

    for j in range(0,10):                           #controls which number we're looking for (0-9)
        count = 0                                   #number of times number appears in last digit
        for i in range(0, len(list)):               #controls index
            element = str(list[i])                  #get the appropriate element from provided index
            last_index_of_element = len(element) - 1            #getting the last index of the element
            last_digit = int(element[last_index_of_element])    #getting the digit from the last index

            if last_digit == j:                     #if the LSD equals the number that we're looking for
                count += 1                          #then increase count

        numbers.append(str(count) + "\t")           #once the inner for loop is once, add the count to the list and tab

    return numbers                                  #return the finished list
        
###################################### MAIN ############################
# using the functions defined above:
#   prompt the user for the size of the list to be created as well as the seed.

size, seed = listParameters()       #two variables that store the two return values

#   create the list of random numbers

randomList = randomList(size,seed)  #get random list

#   If SHOWLIST is selected, print out the list of numbers

if SHOWLIST == True:
    print(randomList)

#   print the head of the table which just shows the numbers 0-9

print( '\t', '0', '\t', '1', '\t', '2', '\t', '3', '\t', '4', '\t', '5', '\t', '6', '\t', '7', '\t', '8', '\t', '9')    #pain
print('----------------------------------------------------------------------------------------------')                 

#   Calculate the MSD and LSD, and print out their statistics.

Mlist = mostSigList(randomList)     #i ran out of ideas for names; this is MSD list
Llist = leastSigList(randomList)    #LSD list

name_for_Most = "MSD"               #name variable for MSD list to pass into printList function
name_for_Least = "LSD"              #name variable for LSD list to pass into printList function

printList(name_for_Most, Mlist)          #print MSD list
printList(name_for_Least, Llist)         #print LSD list 
