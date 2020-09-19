### math functions


#currently has the following functions working:
#factorial                  (factorial (x))
#cosine                     (cos(x))
#sine                       (sin(x))
#exponential                (exp(x))
#square root                (sqrt(a))
#absolute value             (absolute(x))
#arcsin                     (arcsin(x))
#arccos                     (arccos(x))
#arctan                     (arctan(x))



#functions that still need work: (error work)
#cosine
#sine
#factorial


def cos (x):
    #work: error.... 
    c = 0
    tol = 1e-6
    for i in range(40):
        newTerm = (((-1)**i)*x**(2*i))/(factorial(2*i))
        #error = ((cos(x) - c)**2)**0.5    .... but alas, there is no python function for cos..... and that would make this useless
        c = c + newTerm
        if absolute(newTerm)< tol: # absolute value is much more computationally efficient compared to squaring and finding the square root numerically
            break  
    return c
    
        
def sin (x):
    #work: error.... 
    s = 0
    tol = 1e-6
    for i in range (40):
        newTerm = (((-1)**i)*x**(2*i+1))/(factorial(2*i+1))
        s = s + newTerm
        if absolute(newTerm)< tol:
            break
    return s
    
def arcsin (x):
    if x*x >= 1: #not sure whether this is better or abs... (see also arctan)
        Error = True
    else:
        s = 0
        tol = 1e-6
        for i in range (40):
            newTerm = (factorial(2*i))*x**(2*i+1)/(4**i*(factorial(i))**2*(2*i+1))
            s = s+ newTerm
            if absolute(newTerm) < tol:
                break
        return s

def arccos(x):
    return pi/2 - arcsin(x)


def arctan (x):
    if x*x >= 1:
        Error = True
    else:
        s = 0
        tol = 1e-6
        for i in range (40):
            newTerm = (-1)**i*x**(2*i+1)/(2*i+1)
            s = s+ newTerm
            if absolute(newTerm) < tol:
                break
        return s



def factorial (x):
    #work: stuff for if it is not an integer input
    # edit: done some research and found that its an integral - which means I need a numerical integrater
    fac = 1
    if x == int(x):
        for i in range (1,x + 1):
            fac = fac*i 
    else:
        print ("nah bro")
        fac = x
        #chuck some error stuff in here...
    return fac

def absolute (x):
    if x < 0:
        x = x*-1
    return x
        

def exp (x):
    e = 0
    tol = 1e-6
    for i in range (40):
        newTerm = x**i/factorial(i)
        e = e + newTerm
        if absolute(newTerm) < tol:
            break
    return e


def sqrt(a):
    #newtons method
    x0 = a/2   #there will probably be a better method of finding a guess but this will do for now
    tol = 1e-9
    for i in range(100): #the number of iterations that is allowed is the limiting factor of how big the number can be
        x1 = 0.5*(x0 + a/x0)
        diffSQ = (x1- x0)**2
        x0 = x1
        if diffSQ < tol:
            print ("interations:" + str(i))
            break
    return x0









### naming mathematical constants

pi = 3.1415926535897932384626433 #25 decimal places





















    
