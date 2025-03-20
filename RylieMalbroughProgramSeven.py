####################################################################
# author: Rylie Malbrough
# date: 11/4/2022
# desc: Random Grade Assignments 
###################################################################

from random import randint

# constants defined to limit the scope of the randomly generated grades.

lowest_grade = 65
highest_grade = 100

# A function that prompts the user for the number of students in the
# class and returns that value to the calling statement.

def getStudents():
    return int(input("How many students are in this imaginary class? "))

# A function that receives the number of students as an argument, and
# creates a list of random integers of that size. The complete list is
# returned to the calling statement.

def random_grades(students):
    grades = []   #create an empty list 

    while len(grades) < students:    
        grades.append(randint(lowest_grade, highest_grade))  #add number to list between 65 and 100

    return grades 
    

# A function that receives a single grade as its argument, and returns a
# letter corresponding to the correct letter grade.

def determine_grade(grade):   

    if grade >= 90:
        return "A"
    elif grade >= 80 and grade < 90:
        return "B"
    elif grade >= 70 and grade < 80:
        return "C"
    else:
        return "D"

# A function that receives a list of values, and prints them in order
# separated by a tab space.

def list_and_tab(values):
    empty = []
    
    i = 1
    for i in range(len(values)):            #function only while i is within the range of the list
        empty.append(str(values[i]) + "\t") #add the value + a tab to the list
        i += 1

    print(*empty)    #print out on one line
        
       
# A function that recieves a list of numerical values (corresponding to
# the numerical grades), and creates a list of corresponding letter
# grades. This list of letter grades is then returned to the calling
# statement.

def get_letter_grade(number_grade):
    letters = []

    i = 1
    for i in range(len(number_grade)):
        letters.append(determine_grade(number_grade[i]))
        i += 1

    return letters
    
# A function that recieves a list of numerical values, and returns the
# mean/average of that list.

def getAvg(numbers):
    return round(sum(numbers)/len(numbers),1)  

############################# main ############################

# using functions defined above, get the class size, numerical grade
# list, and letter grade list.

size = getStudents()
numerical_values = random_grades(size)
letter_grades = get_letter_grade(numerical_values)

# Print out both numerical and letter grades as well as the average.
print("Numerical Grades: ")
list_and_tab(numerical_values)
print("Letter Grades: ")
list_and_tab(letter_grades)
print("The average grade for the class is ", getAvg(numerical_values))
