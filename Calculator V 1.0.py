# Calculator V1.0
# Author: Andrew Close


########## Maths functions #############

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


########### Decoder Functions ############

#experimental and not in use yet. Will require global text var and input replacing the relavant lines in the main code.
def exp_check (text):
    prior = subText[0:text.find("^")]
    post = text[text.find("^") + 1:len(text)]
    print ("prior and post: " + str(prior) + ' ' + str(post))
    indexnum1 = prior.rfind(" ")
    if indexnum1 == -1:
        indexnum1 = 0
    print("indexnum1: " +str(indexnum1))
    num1 = prior[indexnum1:len(prior)]
    print("num1: " + str(num1))
    indexnum2 = post.find(" ")
    if indexnum2 > post.find("^") and post.find('^') != -1:
        indexnum2 = post.find("^")
    if indexnum2 == -1:
        indexnum2 = len(post)
    num2 = post[0:indexnum2]
    print('num2: ' + str(num2))
    ans = float(num1)^float(num2)
    subText = str(prior[0:indexnum1]) + str(ans) + str(post[indexnum2:len(post)])
    text = str(text[0:indexOpen+1]) + str(subText) + str(text[indexClose-1:len(text)])
    

def cos_check (text):
    if 'cos' in text:
        num = text[text.count('cos')]
        # work in progress

        # the idea is to find how many cos() there are and then send the text to the appropriate algorithm to solve
        # the inside thingy - once its a number then to run the cos function

        #



#error checking - balance brackets
def bedmas_check(text):
    text = '(' + str(text) + ')'
    if text.count("(") != text.count(")"):
        print ("Invalid syntax: Unbalanced brackets")
    else:
        for i in range(2+text.count("(")):
            indexOpen = text.rfind("(")
            indexClose = text.find(")", indexOpen)
            print (str(indexOpen) + ", " + str(indexClose))
            subText = text[indexOpen+1:indexClose]
            print("innermost bracket contains: " + str(subText))
            try:
                subText = float(subText)
                print("text: " + str(text))
                print(subText)
                if indexOpen >= 2:
                    text = str(text[0:indexOpen-1]) + str(subText) + str(text[indexClose+1:len(text)])
                    #print("a")
                    print("indexOpen: " + str(indexOpen))
                    print("indexClose: " + str(indexClose))
                elif indexOpen == 1:
                    text = str(text[0:indexOpen]) + str(subText) + str(text[indexClose+1:len(text)])
                    #print("b")
                else:
                    text = str(subText) + str(text[indexClose+1:len(text)])
                    #print('c')
                print ("delete brackets: " + str(text))
                # remove brackets from text surrounding subText
            except ValueError:
                for i in range (1,1000):
                    # Exponent
                    if subText.find("^") != -1:
                        prior = subText[0:subText.find("^")]
                        post = subText[subText.find("^") + 1:len(subText)]
                        print ("prior and post: " + str(prior) + ' ' + str(post))
                        indexnum1 = prior.rfind(" ")
                        if indexnum1 == -1:
                            indexnum1 = 0
                        print("indexnum1: " +str(indexnum1))
                        num1 = prior[indexnum1:len(prior)]
                        print("num1: " + str(num1))
                        indexnum2 = post.find(" ")
                        if indexnum2 > post.find("^") and post.find('^') != -1:
                            indexnum2 = post.find("^")
                        if indexnum2 == -1:
                            indexnum2 = len(post)
                        num2 = post[0:indexnum2]
                        print('num2: ' + str(num2))
                        ans = float(num1)^float(num2)
                        subText = str(prior[0:indexnum1]) + str(ans) + str(post[indexnum2:len(post)])
                        text = str(text[0:indexOpen+1]) + str(subText) + str(text[indexClose-1:len(text)]) 
                    # Division or multiplication
                    elif subText.find(" x ") != -1 or subText.find(' / ') != -1:
                        if subText.find(" x ") != -1:
                            prior = subText[0:subText.find(" x ")]
                            post = subText[subText.find(" x ") + 3:len(subText)]
                            print ("prior and post: " + str(prior) + ' ' + str(post))
                            indexnum1 = prior.rfind(" ")
                            if indexnum1 == -1:
                                indexnum1 = 0
                            print("indexnum1: " +str(indexnum1))
                            num1 = prior[indexnum1:len(prior)]
                            print("num1: " + str(num1))
                            indexnum2 = post.find(" ")
                            if indexnum2 == -1:
                                indexnum2 = len(post)
                            num2 = post[0:indexnum2]
                            print('num2: ' + str(num2))
                            ans = float(num1)*float(num2)
                            subText = str(prior[0:indexnum1]) + str(ans) + str(post[indexnum2:len(post)])
                            print("subText: " + subText)
                            print('1 ' + str(text[0:indexOpen+1]))
                            print('2 ' + str(subText))
                            print('3 ' + str(text[indexClose:len(text)]))
                            text = str(text[0:indexOpen+1]) + str(subText) + str(text[indexClose:len(text)])
                            
                            print ("text: " + str(text))
                        else:
                            prior = subText[0:subText.find(" / ")]
                            post = subText[subText.find(" / ") + 3:len(subText)]
                            print ("prior and post: " + str(prior) + ' ' + str(post))
                            indexnum1 = prior.rfind(" ")
                            if indexnum1 == -1:
                                indexnum1 = 0
                            print("indexnum1: " +str(indexnum1))
                            num1 = prior[indexnum1:len(prior)]
                            print("num1: " + str(num1))
                            indexnum2 = post.find(" ")
                            if indexnum2 == -1:
                                indexnum2 = len(post)
                            num2 = post[0:indexnum2]
                            print('num2: ' + str(num2))
                            ans = float(num1)/float(num2)
                            subText = str(prior[0:indexnum1]) + str(ans) + str(post[indexnum2:len(post)])
                            text = str(text[0:indexOpen+1]) + str(subText) + str(text[indexClose-1:len(text)]) 
                         
                    # Addition and substraction
                    elif subText.find(" - ") != -1 or subText.find(' + ') != -1:
                        if subText.find(" - ") != -1:
                            prior = subText[0:subText.find(" - ")]
                            post = subText[subText.find(" - ") + 3:len(subText)]
                            print ("prior and post: " + str(prior) + ' ' + str(post))
                            indexnum1 = prior.rfind(" ")
                            if indexnum1 == -1:
                                indexnum1 = 0
                            print("indexnum1: " +str(indexnum1))
                            num1 = prior[indexnum1:len(prior)]
                            print("num1: " + str(num1))
                            indexnum2 = post.find(" ")
                            if indexnum2 == -1:
                                indexnum2 = len(post)
                            num2 = post[0:indexnum2]
                            print('num2: ' + str(num2))
                            ans = float(num1)-float(num2)
                            subText = str(prior[0:indexnum1]) + str(ans) + str(post[indexnum2:len(post)])
                            print("subText: " + subText)
                            print('1 ' + str(text[0:indexOpen+1]))
                            print('2 ' + str(subText))
                            print('3 ' + str(text[indexClose-1:len(text)]))
                            text = str(text[0:indexOpen+1]) + str(subText) + str(text[indexClose:len(text)])
                            
                            print ("text: " + str(text))
                        else:
                            prior = subText[0:subText.find(" + ")]
                            post = subText[subText.find(" + ") + 3:len(subText)]
                            print ("prior and post: " + str(prior) + ' ' + str(post))
                            indexnum1 = prior.rfind(" ")
                            if indexnum1 == -1:
                                indexnum1 = 0
                            print("indexnum1: " +str(indexnum1))
                            num1 = prior[indexnum1:len(prior)]
                            print("num1: " + str(num1))
                            indexnum2 = post.find(" ")
                            if indexnum2 == -1:
                                indexnum2 = len(post)
                            num2 = post[0:indexnum2]
                            print('num2: ' + str(num2))
                            ans = float(num1)+float(num2)
                            subText = str(prior[0:indexnum1]) + str(ans) + str(post[indexnum2:len(post)])
                            text = str(text[0:indexOpen+1]) + str(subText) + str(text[indexClose-1:len(text)]) 
    return text



################ Calculator Interface ##############

from tkinter import *

def addText(x):
    global output
    txt = output.get()
    output.set(str(txt) + str(x))


def add0 ():
    addText("0")

def add1 ():
    addText("1")

def add2 ():
    addText("2")

def add3 ():
    addText("3")

def add4 ():
    addText("4")

def add5 ():
    addText("5")

def add6 ():
    addText("6")

def add7 ():
    addText("7")

def add8 ():
    addText("8")

def add9 ():
    addText("9")

def addPoint ():
    addText(".")

def addAdd ():
    addText(" + ")

def addSub ():
    addText(" - ")

def addDiv ():
    addText(" / ")

def addMult ():
    addText(" x ")

def addOpenBracket():
    addText("(")

def addCloseBracket():
    addText(")")

def addPower():
    addText("^")

def equal ():
    #this needs a reading function, a solver, and then a place to put the answer
    global output
    txt = output.get()
    output.set(bedmas_check(txt))
    #reader
    #solver
    #output.set(ans)


def addSin ():
    addText("sin(")

def addCos ():
    addText("cos(")

def addTan ():
    addText("tan(")

def addASin ():
    addText("arc sin(")

def addACos ():
    addText("arc cos(")

def addATan ():
    addText("arc tan(")

def addExp():
    addText("exp(")

def addLn():
    addText("ln(")

def addLog():
    addText("log(")

def addSqrt():
    addText("SQRT(")

def clearText():
    global output
    output.set("")

def reader (text):
    text.find("(")
    


calc = Tk()
calc.title("Calculator Program")
frameScreen = Frame(calc)
frameButtons = Frame(calc)
frameMath = Frame(calc)

#Assign Variables
output = StringVar()
output.set("")

outputLabel = Label(frameScreen, textvariable = output).grid(row = 1, column = 1)

#number buttons
num_pad_x = 2   #easier to change all of them here
num_pad_y = 2
num_ipad_x = 6
num_ipad_y = 4


buttonPoint = Button(frameButtons, text = ".", command = addPoint).grid(row = 4, column = 2, padx = num_pad_x, pady = num_pad_y, ipady = num_ipad_y, ipadx = num_ipad_x)
button0 = Button(frameButtons, text = "0", command = add0).grid(row = 4, column = 1, padx = num_pad_x, pady = num_pad_y, ipady = num_ipad_y, ipadx = num_ipad_x)
button1 = Button(frameButtons, text = "1", command = add1).grid(row = 3, column = 1, padx = num_pad_x, pady = num_pad_y, ipady = num_ipad_y, ipadx = num_ipad_x)
button2 = Button(frameButtons, text = "2", command = add2).grid(row = 3, column = 2, padx = num_pad_x, pady = num_pad_y, ipady = num_ipad_y, ipadx = num_ipad_x)
button3 = Button(frameButtons, text = "3", command = add3).grid(row = 3, column = 3, padx = num_pad_x, pady = num_pad_y, ipady = num_ipad_y, ipadx = num_ipad_x)
button4 = Button(frameButtons, text = "4", command = add4).grid(row = 2, column = 1, padx = num_pad_x, pady = num_pad_y, ipady = num_ipad_y, ipadx = num_ipad_x)
button5 = Button(frameButtons, text = "5", command = add5).grid(row = 2, column = 2, padx = num_pad_x, pady = num_pad_y, ipady = num_ipad_y, ipadx = num_ipad_x)
button6 = Button(frameButtons, text = "6", command = add6).grid(row = 2, column = 3, padx = num_pad_x, pady = num_pad_y, ipady = num_ipad_y, ipadx = num_ipad_x)
button7 = Button(frameButtons, text = "7", command = add7).grid(row = 1, column = 1, padx = num_pad_x, pady = num_pad_y, ipady = num_ipad_y, ipadx = num_ipad_x)
button8 = Button(frameButtons, text = "8", command = add8).grid(row = 1, column = 2, padx = num_pad_x, pady = num_pad_y, ipady = num_ipad_y, ipadx = num_ipad_x)
button9 = Button(frameButtons, text = "9", command = add9).grid(row = 1, column = 3, padx = num_pad_x, pady = num_pad_y, ipady = num_ipad_y, ipadx = num_ipad_x)


buttonEqual = Button(frameButtons, text = "=", command = equal).grid(row = 4, column = 3, padx = 2, pady = 2, ipady = 4, ipadx = 4)

#operation buttons
buttonAdd = Button(frameButtons, text = "+", command = addAdd).grid(row = 1, column = 4, padx = 2, pady = 2, ipady = 4, ipadx = 4)
buttonSub = Button(frameButtons, text = "-", command = addSub).grid(row = 2, column = 4, padx = 2, pady = 2, ipady = 4, ipadx = 4)
buttonDiv = Button(frameButtons, text = "/", command = addDiv).grid(row = 3, column = 4, padx = 2, pady = 2, ipady = 4, ipadx = 4)
buttonMult = Button(frameButtons, text = "x", command = addMult).grid(row = 4, column = 4, padx = 2, pady = 2, ipady = 4, ipadx = 4)
buttonOpenBracket = Button(frameButtons, text = "(", command = addOpenBracket).grid(row = 1, column = 5, padx = 2, pady = 2, ipady = 4, ipadx = 4)
buttonCloseBracket = Button(frameButtons, text = ")", command = addCloseBracket).grid(row = 2, column = 5, padx = 2, pady = 2, ipady = 4, ipadx = 4)
buttonPower = Button(frameButtons, text = "^", command = addPower).grid(row = 3, column = 5, padx = 2, pady = 2, ipady = 4, ipadx = 2)

#math buttons
buttonSin = Button(frameMath, text = "   sin   ", command = addSin).grid(row = 2, column = 1, padx = 2, pady = 2, ipady = 4, ipadx = 4)
buttonCos = Button(frameMath, text = "   cos   ", command = addCos).grid(row = 2, column = 2, padx = 2, pady = 2, ipady = 4, ipadx = 4)
buttonTan = Button(frameMath, text = "   tan   ", command = addTan).grid(row = 2, column = 3, padx = 2, pady = 2, ipady = 4, ipadx = 4)
buttonArcSin = Button(frameMath, text = "arc sin", command = addASin).grid(row = 3, column = 1, padx = 2, pady = 2, ipady = 4, ipadx = 4)
buttonArcCos = Button(frameMath, text = "arc cos", command = addACos).grid(row = 3, column = 2, padx = 2, pady = 2, ipady = 4, ipadx = 4)
buttonArcTan = Button(frameMath, text = "arc tan", command = addATan).grid(row = 3, column = 3, padx = 2, pady = 2, ipady = 4, ipadx = 4)
buttonClear = Button(frameMath, text = " Clear ", command = clearText).grid(row = 1, column = 1, padx = 2, pady = 2, ipady = 4, ipadx = 4)
buttonExp = Button(frameMath, text = "   exp   ", command = addExp).grid(row = 1, column = 2, padx = 2, pady = 2, ipady = 4, ipadx = 4)
buttonLn = Button(frameMath, text = "    ln    ", command = addLn).grid(row = 1, column = 3, padx = 2, pady = 2, ipady = 4, ipadx = 4)
buttonLog = Button(frameMath, text = "   log   ", command = addLog).grid(row = 4, column = 1, padx = 2, pady = 2, ipady = 4, ipadx = 4)
buttonSQRT = Button(frameMath, text = "   sqrt  ", command = addSqrt).grid(row = 4, column = 2, padx = 2, pady = 2, ipady = 4, ipadx = 4)




#add whatever buttons are needed

#Frame Structure
frameScreen.grid(row = 1, column = 1, columnspan = 2,padx = 10, pady = 10)
frameButtons.grid(row = 2, column = 2, padx = 10, pady = 15)
frameMath.grid(row =2, column = 1, padx = 10, pady = 15)


calc.mainloop()
