### math functions

'''
Author: Andrew Close
Date: 25/08/2021
Description:
This script contains mathematical functions for the calculator to
use when needed. These functions are constructed from numerical methods
such as Taylor series and Newtons method.

Functions containted:
cos(x) - Returns cosine(x) where x in an angle in radians
sin(x) - Returns sine(x) where x in an angle in radians
tan(x) - Returns tangent(x) where x in an angle in radians
arcsin(x) - Inverse sine, returns the angle in radians given a float between -1 and 1
arccos(x) - Inverse cosine, returns the angle in radians given a float between -1 and 1
arctan(x) - Inverse tangent, returns the angle in radians given a float between -inf and inf
factorial(x) - Returns factorial of x, given that x is a positive int. This function does not support none int input
absolute(x) - Returns the absolute value of x
exp(x) - Returns e^x, where e ~ 2.71
sqrt(x) - Returns the square root of x
ln(x) - Returns the natural log of x for x greater than 0
ln_between_1_and_2(x) - Used in ln(x) for an accurate approximation of ln on 1 <= x <= 2
log(base, x) - Returns the log of x given x and the base. This is built off ln(x) using a base converstion for simplicity
deg_to_rad(x) - Returns an angle value in radians given one in degrees
rad_to_deg(x) - Returns an angle value in degrees given one in radians
'''

def cos(x):
    c = 0
    tol = 1e-6
    # Taylor series expansion
    for i in range(40):
        newTerm = (((-1)**i)*x**(2*i))/(factorial(2*i))
        c = c + newTerm
        if absolute(newTerm)< tol: 
            break  
    return c
    
        
def sin(x):
    s = 0.0
    tol = 1e-6
    # Taylor series expansion
    for i in range (40):
        newTerm = (((-1)**i)*x**(2*i+1))/(factorial(2*i+1))
        s = s + newTerm
        if absolute(newTerm)< tol:
            break
    return s


def tan(x):
    # using tan(x) = sin(x)/cos(x)
    sin_x = sin(x)
    cos_x = cos(x)
    return sin_x/cos_x
    
    
def arcsin(x):
    # input must be between -1 and 1
    if x*x >= 1: 
        return False
    else:
        s = 0
        tol = 1e-6
        # Taylor series expansion
        for i in range (40):
            newTerm = (factorial(2*i))*x**(2*i+1)/(4**i*(factorial(i))**2*(2*i+1))
            s = s+ newTerm
            if absolute(newTerm) < tol:
                break
        return s


def arccos(x):
    return pi/2 - arcsin(x)


def arctan(x):
    # input must be between -1 and 1
    if x*x >= 1:
        return False
    else:
        s = 0
        tol = 1e-6
        # Taylor series expansion
        for i in range (40):
            newTerm = (-1)**i*x**(2*i+1)/(2*i+1)
            s = s+ newTerm
            if absolute(newTerm) < tol:
                break
        return s


def factorial(x):
    fac = 1
    if type(x) == int:
        for i in range (1,x + 1):
            fac = fac*i 
    else:
        return False
    return fac


def absolute(x):
    if x < 0:
        return -x
    return x
        

def exp(x):
    e = 0
    tol = 1e-6
    # Taylor series expansion
    for i in range (40):
        newTerm = x**i/factorial(i)
        e = e + newTerm
        if absolute(newTerm) < tol:
            break
    return e


def sqrt(x):
    x0 = x/2
    tol = 1e-9
    # newtons method
    for i in range(100): #the number of iterations that is allowed is the limiting factor of how big the number can be - works up til about 1e28
        x1 = 0.5*(x0 + x/x0)
        diffSQ = (x1- x0)**2
        x0 = x1
        if diffSQ < tol:
            print(i)
            break
    return x0


def ln(x):
    # This is done using an approximation for 1 < x < 2
    # and using this with ln(x) = n*ln(2) + ln(x/2^n) for 2^n < x < 2(n+1).
    # The method uses a little bit of recursion within that but seems fast enough
    # when tested.
    # Testing indicates that the average error for 0.0001 to 10000 is 0.057%, max error 0.547%
    if x <=0:
        return False
    if x >= 1 and x <= 2:
        # this is the main approximation
        return ln_between_1_and_2(x)
        # alternative much faster method using 5th order polynomial approximation. Average error is 1.151%, max error 8.967%
        #return -1.921064448 + (3.52930504 + (-2.461222169 + (1.130626210 + (-0.2887399591 + 0.03110401824*x)*x)*x)*x)*x
    elif x < 1:
        n = -1
        upper_bound = 1
        while True:
            lower_bound = 2**(n)
            if x >= lower_bound and x <= upper_bound:
                # within 2^n and 2^(n+1) 
                return n * ln_2 +  ln(x / lower_bound)
            # update lower and upper bounds (2^n and 2^(n+1) where n = n+1
            upper_bound = lower_bound
            n += -1
        return False
    else:
        # cases where x is above 2
        n = 1
        lower_bound = 2
        while True:
            upper_bound = 2**(n+1)
            if x >= lower_bound and x <= upper_bound:
                # within 2^n and 2^(n+1) 
                return n * ln_2 +  ln(x / lower_bound)
            # update lower and upper bounds (2^n and 2^(n+1) where n = n+1
            lower_bound = upper_bound
            n += 1

def ln_between_1_and_2(x):
    ln_x = 0 # starting with x = 1
    if x == 1:
        return ln_x
    elif x == 2:
        return ln_2
    # ln(x + 0.01) ~ ln(x) + 1/600*(1/x + 4/(x + 0.005) + 1/(x + 0.01)) this is a Runge-Kutta approximation
    for i in range(100, 200): # as we can't use a float in the range function
        j = float(i)/100
        ln_x = ln_x + 1/600*(1/j + 4/(j + 0.005) + 1/(j + 0.01))
        if j+0.01 >= x:
            return ln_x
    
        
def log(base, x):
    # this function rides on the back of the natural log function using a base change formula
    ln_base = ln(base)
    ln_x = ln(x)
    return ln_x/ln_base


def deg_to_rad(x):
    # given a value in degrees, we need to find it in radians to run any of the trig functions
    return x*pi/180

def rad_to_deg(x):
    # given a value in radians, return the value in degrees
    return x*180/pi


### naming mathematical constants

pi = 3.1415926535897932384626433 #25 decimal places
ln_2 = 0.69314718056




















    
