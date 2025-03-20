######################################################################
# author: Rylie Malbrough  
# date: 2/5/2023  
# desc: Exam prep simulation game  
#####################################################################
from random import *

DEBUG = True   # Activate intermediate output

#function for getting data values
def getData():
    questionBank = []                                                                       #empty list to store questions
    
    questions = input("What is the size of the question bank? ")                            #get number of questions
    for i in range(1,int(questions)+1):                                                     #append numbers 1 through number of questions
        questionBank.append(i)                                                              #to the question bank

    studied = input("How many of those questions have you studied? ")                       #get number of questions you studied
    questionsStudied = sample(range(1, len(questionBank)+1), k=int(studied))                #get a random sample of numbers from the question bank
       
    testQuestions = int(input("How many questions does the test have? "))                   #get number of questions

    answersToPass = int(input("How many questions must you answer correctly to pass the test? "))   #get number of questions you must answer correctly
    if testQuestions < answersToPass:                                                               #input validation
        print("That's impossible! There's not that many questions!\n")
    
    return testQuestions, questionBank, questionsStudied, answersToPass

#function that creates a random test list
def random(test, bank):
    testQuestions = sample(range(1, len(bank)), k=int(test))        #get a sample of test questions from the question bank
    return testQuestions

#function that determines whether or not you've failed or passed a test
def percentCorrect(study, testList, answer):
    correct = 0                                                    #initialize correct to zero
    correctIndex = []

    for j in range(0, len(testList)):                              #loop through every index in the testList
        for i in range(0, len(study)):                             #loop through every index in the studyList
            if testList[j] == study[i]:                            #if they are equal, 
                correctIndex.append(i)                             #append that value to correctIndex so you can see which questions are right 
                correct += 1                                       #you got one corret
                
    if int(correct) >= int(answer):                                #if number of correct questions exceeds the number of questions you need to get right
        testPass = 1                                               #you pass
    else:
        testPass = 0                                               #you fail
    
    return testPass, correctIndex, correct

#function that runs the simulation
def simulation(test, bank, answer, study):
    simulations = int(input("How many simulations do you want to run? "))       #get user input for simulations
    totalCorrect = []                                                           #create a list for the total tests passed
    
    for i in range(1, simulations+1):                                           #run the correct amount of simulations
      newList = random(test, bank)                                              #create a new set of test questions every loop
      testPass, correctIndex, correct = percentCorrect(study, newList, answer)  #call percentCorrect function to determine if you passed with the new test list
      totalCorrect.append(testPass)                                             #append the value (1 for pass, 0 for fail) to totalCorrect

      ########DEBUG#########
      if DEBUG == True:
          print("Simulation No. {}".format(i))
          print("Questions you were asked: {}".format(newList))
          print("Questions you studied: {}".format(study))
          print("Questions you passed: {}".format(correctIndex))
          print("Which mean you scored {}/{}".format(correct, test))
          print("-" * 80)
      #######################
          
    percent = float(sum(totalCorrect))/(simulations) * 100                      #get percentage value by dividing the amount of times you passed by the total simulations x 100
      
    return percent
        

#########################main###################################
print("Simulation Set Up: ")
print("=" *80)

#get data
test, bank, study, answer = getData()
print("=" *80)

#get percent
percent = simulation(test, bank, answer, study)
print("=" *80)
print("You passed the test {}% of the time".format(percent))
