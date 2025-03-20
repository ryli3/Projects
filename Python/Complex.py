############################################################################
# name: Rylie Malbrough 
# date: 1/11/2022
# description: Complex Numbers
############################################################################

# Don't forget to name this file Complex.py and place it in the same
# folder as the provided ComplexTest.py file so that they can
# automatically find and use each other.

class Complex:
    # A constructor that takes two values for the real and imaginary
    # portions respectively. Default values for both parameters are 0.

    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

#######accessors and mutators for the instance variables###################

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, real):
        self._real = real 

    @property
    def imaginary(self):
        return self._imaginary

    @imaginary.setter
    def imaginary(self, imaginary):
        self._imaginary = imaginary

#######overloaded mathematical operators i.e. ==, +, -, *, /################

    def __add__(self, other):
        real = self.real + other.real                           #create variable for the real number, add the real coeff. from both self and other
        imaginary = self.imaginary + other.imaginary            #create variable for imaginary number, add the imaginary coeff. from both self and other
            
        return Complex(real, imaginary)                         #create a new object from new values
    

    def __sub__(self, other):
        real = self.real - other.real                           #create variable for the real number, subtract the real coeff. from both self and other
        imaginary = self.imaginary - other.imaginary            #create variable for the imaginary number, subtract the imaginary coeff. from both self and other

        return Complex(real, imaginary)                         #create a new object from new values
    

    def __mul__(self, other):
        real = (self.real * other.real) - (self.imaginary * other.imaginary)                    #take appropriate real and imaginary coefficients and subtract them, store in variable 
        imaginary = (self.real * other.imaginary) + (self.imaginary * other.real)               #take appropriate real and imaginary coefficents and add them, store in variable
            
        return Complex(real, imaginary)                                                         #create a new object from new values
    

    def __truediv__(self, other):
 
        den =(other.real*other.real) + (other.imaginary*other.imaginary)                        #get the denominator by adding the real coeff. and imaginary coeff.
        real =(self.real * other.real) + (self.imaginary * other.imaginary)                     #get the real value by adding appropriate imaginary and real coeff.
        imaginary =(other.real * self.imaginary) - (self.real * other.imaginary)                #get the imaginary value by subtracting imaginary and real coeff.

        imaginary = imaginary/den                                                               #divide imaginary by denominator
        real = real/den                                                                         #divide real by denominator

        return Complex(real, imaginary)                                                         #create new object from new values
    

    def __equ__(self, other):
        if (self.real == other.real and self.imaginary == other.imaginary):                     #make sure that the real values and imaginary values are equal in both values 
            return True                                                                         #if so, then it they're equal, return TRUE
        else:
            return False                                                                        #otherwise, they are not equal, return FALSE
    

####### Other functions e.g. reciprocal, conjugate, and __str__###########################

    def reciprocal(self):
        den = (self.real * self.real) + (self.imaginary * self.imaginary)                      #get den value from adding real and imaginary coeff
        real = (self.real / den)                                                               #real value is the real coeff. divided by den
        imaginary = (self.imaginary / den)                                                     #imaginary value is the imaginary coeff. divided by the den

        if (second < 0):                                                                       #since the reciprocal involves flipping the sign, i created a conditional
            positive = imaginary * -1                                                          #two negatives make a positive
            reciprocal = "{} + {}i".format(first, positive)                                    #change to addition 
        else:
            reciprocal = "{} - {}i".format(first, second)                                      #otherwise, the imaginary number is positive so it is subtracted 
            
        return reciprocal

    def conjugate(self):
        if self.imaginary < 0:                                                                #if the imaginary portion is negative
            positive = self.imaginary * -1                                                    #turn to positive (conjugate)
            conjugate = str(self.real) + " + " + str(positive) + "i"
        else:
            conjugate = str(self.real) + " - " + str(self.imaginary) + "i"                    #otherwise, imaginary is positive, so make it negative
            
        return conjugate 

    def __str__(self):                                                                       
        if (self.imaginary < 0):                                                              #if imaginary is negative  
            positive = (self.imaginary * -1)                                                  #make it positive
            string = str(self.real) + " - " + str(positive) + "i"                             #so I can put the negative between values
        else:
            string = str(self.real) + " + " + str(self.imaginary) + "i"                       #otherwise, keep the addition  
            
        return string
    



