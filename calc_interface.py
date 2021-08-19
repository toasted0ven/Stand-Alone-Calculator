## atempt at making the calculator interface


from tkinter import *
from decoder_iterative_V5_0 import *

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
    addText(" ^ ")

def equal ():
    #this needs a reading function, a solver, and then a place to put the answer
    global output
    txt = output.get()
    list_x = text_to_list(txt)
    answer = decoder(list_x)
    #reader
    #solver
    output.set(answer)


def addSin ():
    addText("sin(")

def addCos ():
    addText("cos(")

def addTan ():
    addText("tan(")

def addASin ():
    addText("asin(")

def addACos ():
    addText("acos(")

def addATan ():
    addText("atan(")

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
    

def interface():
    global output
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

if __name__ == '__main__':
    interface()
