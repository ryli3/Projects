import RPi.GPIO as GPIO
from time import sleep, time

#constants
DEBUG = False           #allows us to debug when true 

SETTLE_TIME = 2         #seconds to let the sensor settle
CALIBRATIONS = 5        #number of calibration measurements to take
CALIBRATION_DELAY = 1   #seconds between each calibration measurement

TRIGGER_TIME = 0.00001  #seconds before triggering the sensor
SPEED_OF_SOUND = 343    #speed of sound in m/s
UNSORT = []             #empty list for storing measurements


#set the RPi to the broadcom pin layout
GPIO.setmode(GPIO.BCM)

#GPIO pins
TRIG = 18         #sensor's TRIG pin
ECHO = 27         #sensor's ECHO pin

GPIO.setup(TRIG, GPIO.OUT)          #TRIG is an output
GPIO.setup(ECHO, GPIO.IN)           #ECHO is an input

#################################################################################
# calibrates the sensor, returns a correction factor to use in calculations     #
#################################################################################

def calibrate():
    print("Calibrating. . .")
    print("-Place the sensor a measured distance away from an object.")         #prompt user to place an object a certain distance away from sensor
    known_distance = float(input("-What is the measured distance (cm)? "))      #prompt user for that distance
    print("-Getting calibration measurements. . .")

    distance_avg = 0    #initliaze distance average at zero
    
    for i in range (CALIBRATIONS):             #starts for loop that iterates 5 times 
        distance = getDistance()               #calls distance function
        
        if (DEBUG):                            
            print("--Got {}cm".format(distance))
            
        distance_avg += distance               #add the average to the found distance
        sleep(CALIBRATION_DELAY)               #delay before getting another measurement
        
    distance_avg /= CALIBRATIONS               #calculates average of measurements
    
    if (DEBUG):                                
        print("--Averge is {}cm".format(distance_avg))

    correction_factor = known_distance / distance_avg  #calculates the correction factor
    
    if (DEBUG):
        print("--Correction factor is {}".format(correction_factor))

    print("Done. ")
    print()

    return correction_factor

#############################################################################
# function that calculates the distance from the sensor to the object       #        
#############################################################################

def getDistance():
    GPIO.output(TRIG, GPIO.HIGH)            #triggers the sensor by setting it high 
    sleep(TRIGGER_TIME)                     #for a short time
    GPIO.output(TRIG, GPIO.LOW)             #and then setting it low

    while (GPIO.input(ECHO) == GPIO.LOW):   #while the ECHO pin is low
        start = time()                      #start time is set

    while (GPIO.input(ECHO) == GPIO.HIGH):  #while the ECHO pin is high
        end = time()                        #end time is set

    duration = end - start                  #calculates how long the ECHO pin was on high - which is its the distance from the object
    distance = duration * SPEED_OF_SOUND    #calculates total distance     
    distance /= 2                           #distance from sensor to object is half of total distance
    distance *= 100                         #converting meters to centimeters

    return distance

###############################################################################
# sorting function for a list of values (sequential search)                   #
###############################################################################

def sel_sort(values):
    n = len(values)             #amount of items in list

    for i in range(0, n - 1):
        minPosition = i         #minimum is the 1st index

        for j in range(i + 1, n):
            if (values[j] < values[minPosition]):   #if the value at the minPosition is greater than the value at index j
                minPosition = j                     #j is the new minimum

        temp = values[i]
        values[i] = values[minPosition]             #swapping values
        values[minPosition] = temp

    print(values)               #print completed list
    return values
    
###############################################################################
#                           MAIN PART OF PROGRAM                              #
###############################################################################

print("Waiting for sensor to settle ({}s). . .".format(SETTLE_TIME))
GPIO.output(TRIG, GPIO.LOW)         #turn TRIG low
sleep(SETTLE_TIME)                  #sleep

correction_factor = calibrate()     #call first function - getting correction_factor

input("Press enter to begin . . . ")
print("Getting measurements: ")

while(True):
    print("-Measuring . . .")
    distance = getDistance() * correction_factor  #calling distance function then multiplying it by correction factor
    sleep(1)                                      #wait one second
    
    distance = round(distance, 4)                 #round distance to four decimal places
    
    UNSORT.append(distance)                       #adding distance found to unsorted list
    
    print("--Distance measured: {}cm".format(distance))

    i = input("--Get another measurement (Y/n)? ")      #asking whether to continue or not
    if (not i in ["y", "Y", "yes", "Yes", "YES", ""]):  #if no
        print()                                         #line
        print("Unsorted Measurements: ")                #unsorted
        print(UNSORT)                                   #print unsorted list
        print()                                         #line
        print("Sorted Measurements: ")                  #sorted
        sel_sort(UNSORT)                                #call sel_sort function for the unsorted list          
        break                                           #end program 
       
        
print("Done.")
GPIO.cleanup()
