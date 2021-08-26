## atempt at making the calculator interface
'''
Author: Andrew Close
Date: 26/08/2021
Description:
This script sets up the interface, deals with passing the inputs to the functions within the decoder script
and returns the output to the screen. 
'''

from tkinter import *
from decoder_iterative_V5_0 import *

def addText(x):
    global output
    txt = output.get()
    output.set(str(txt) + str(x))

# Functions for buttons
def add0():
    addText("0")

def add1():
    addText("1")

def add2():
    addText("2")

def add3():
    addText("3")

def add4():
    addText("4")

def add5():
    addText("5")

def add6():
    addText("6")

def add7():
    addText("7")

def add8():
    addText("8")

def add9():
    addText("9")

def addPoint():
    addText(".")

def addAdd():
    addText(" + ")

def addSub():
    addText(" - ")

def addDiv():
    addText(" / ")

def addMult():
    addText(" x ")

def addOpenBracket():
    addText("(")

def addCloseBracket():
    addText(")")

def addPower():
    addText(" ^ ")

def equal():
    #this needs a reading function, a solver, and then a place to put the answer
    global output
    global angleSetting
    txt = output.get()
    list_x = text_to_list(txt)
    angle_setting = angleSetting.get()
    answer = decoder(list_x, angle_setting)
    output.set(answer)


def addSin():
    addText("sin(")

def addCos():
    addText("cos(")

def addTan():
    addText("tan(")

def addASin():
    addText("asin(")

def addACos():
    addText("acos(")

def addATan():
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

def reader(text):
    text.find("(")

def changeAngleSetting():
    global angleSetting
    current = angleSetting.get()
    if current == 'rad':
        angleSetting.set('deg')
    else:
        angleSetting.set('rad')
    

def interface():
    global output
    global angleSetting
    calc = Tk()
    calc.title("Calculator Program")
    # initialize the different frames
    frameScreen = Frame(calc)
    frameButtons = Frame(calc)
    frameMath = Frame(calc)
    frameSetting = Frame(calc)
    frameDisclaimer = Frame(calc)
    frameEqual = Frame(calc)

    #Assign Variables
    output = StringVar()
    output.set("")

    angleSetting = StringVar()
    angleSetting.set('rad')
    
    outputLabel = Label(frameScreen, textvariable = output).grid(row = 1, column = 1)

    #number buttons
    num_pad_x = 2   #easier to change all of them here
    num_pad_y = 2
    num_ipad_x = 10
    num_ipad_y = 8

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

    buttonEqual = Button(frameEqual, text = "=", command = equal).grid(row = 4, column = 3, padx = num_pad_x, pady = num_pad_y, ipady = 6, ipadx = 90)

    #operation buttons
    op_pad_x = 2
    op_pad_y = 2
    op_ipad_x = 10
    op_ipad_y = 8
    
    buttonAdd = Button(frameButtons, text = "+", command = addAdd).grid(row = 1, column = 4, padx = op_pad_x, pady = op_pad_y, ipady = op_ipad_y, ipadx = op_ipad_x - 1)
    buttonSub = Button(frameButtons, text = "-", command = addSub).grid(row = 2, column = 4, padx = op_pad_x, pady = op_pad_y, ipady = op_ipad_y, ipadx = op_ipad_x)
    buttonDiv = Button(frameButtons, text = "/", command = addDiv).grid(row = 3, column = 4, padx = op_pad_x, pady = op_pad_y, ipady = op_ipad_y, ipadx = op_ipad_x)
    buttonMult = Button(frameButtons, text = "x", command = addMult).grid(row = 4, column = 4, padx = op_pad_x, pady = op_pad_y, ipady = op_ipad_y, ipadx = op_ipad_x)
    buttonOpenBracket = Button(frameButtons, text = "(", command = addOpenBracket).grid(row = 1, column = 5, padx = op_pad_x, pady = op_pad_y, ipady = op_ipad_y, ipadx = op_ipad_x)
    buttonCloseBracket = Button(frameButtons, text = ")", command = addCloseBracket).grid(row = 2, column = 5, padx = op_pad_x, pady = op_pad_y, ipady = op_ipad_y, ipadx = op_ipad_x)
    buttonPower = Button(frameButtons, text = "^", command = addPower).grid(row = 3, column = 5, padx = op_pad_x, pady = op_pad_y, ipady = op_ipad_y, ipadx = op_ipad_x - 1)

    #math buttons
    ma_pad_x = 2
    ma_pad_y = 2
    ma_ipad_x = 10
    ma_ipad_y = 8
    
    buttonSin = Button(frameMath, text = "   sin   ", command = addSin).grid(row = 2, column = 1, padx = ma_pad_x, pady = ma_pad_y, ipady = ma_ipad_y, ipadx = ma_ipad_x)
    buttonCos = Button(frameMath, text = "   cos   ", command = addCos).grid(row = 2, column = 2, padx = ma_pad_x, pady = ma_pad_y, ipady = ma_ipad_y, ipadx = ma_ipad_x)
    buttonTan = Button(frameMath, text = "   tan   ", command = addTan).grid(row = 2, column = 3, padx = ma_pad_x, pady = ma_pad_y, ipady = ma_ipad_y, ipadx = ma_ipad_x)
    buttonArcSin = Button(frameMath, text = "arc sin", command = addASin).grid(row = 3, column = 1, padx = ma_pad_x, pady = ma_pad_y, ipady = ma_ipad_y, ipadx = ma_ipad_x)
    buttonArcCos = Button(frameMath, text = "arc cos", command = addACos).grid(row = 3, column = 2, padx = ma_pad_x, pady = ma_pad_y, ipady = ma_ipad_y, ipadx = ma_ipad_x)
    buttonArcTan = Button(frameMath, text = "arc tan", command = addATan).grid(row = 3, column = 3, padx = ma_pad_x, pady = ma_pad_y, ipady = ma_ipad_y, ipadx = ma_ipad_x)
    buttonClear = Button(frameMath, text = " Clear ", command = clearText).grid(row = 1, column = 1, padx = ma_pad_x, pady = ma_pad_y, ipady = ma_ipad_y, ipadx = ma_ipad_x)
    buttonExp = Button(frameMath, text = "   exp   ", command = addExp).grid(row = 1, column = 2, padx = ma_pad_x, pady = ma_pad_y, ipady = ma_ipad_y, ipadx = ma_ipad_x)
    buttonLn = Button(frameMath, text = "    ln    ", command = addLn).grid(row = 1, column = 3, padx = ma_pad_x, pady = ma_pad_y, ipady = ma_ipad_y, ipadx = ma_ipad_x)
    buttonLog = Button(frameMath, text = "   log   ", command = addLog).grid(row = 4, column = 1, padx = ma_pad_x, pady = ma_pad_y, ipady = ma_ipad_y, ipadx = ma_ipad_x)
    buttonSQRT = Button(frameMath, text = "   sqrt  ", command = addSqrt).grid(row = 4, column = 2, padx = ma_pad_x, pady = ma_pad_y, ipady = ma_ipad_y, ipadx = ma_ipad_x)

    #setting buttons
    buttonDescription = Label(frameSetting, text = 'Angle setting: ').grid(row = 1, column = 1, padx = 10, pady = 15, ipady = 6, ipadx = 6)
    buttonAngleSetting = Button(frameSetting, textvariable = angleSetting, command = changeAngleSetting).grid(row = 1, column = 2, padx = 10, pady = 5, ipady = 6, ipadx = 6)

    # disclaimer
    disclaimer = Label(frameDisclaimer, text = 'Warning: mathematical functions used for this program are approximations not exact answers').grid(row = 1, column = 1, padx = 4, pady = 5, ipady = 2, ipadx = 2)

    #Frame Structure
    frameScreen.grid(row = 1, column = 1, columnspan = 2,padx = 10, pady = 10)
    frameButtons.grid(row = 2, column = 2, padx = 10, pady = 15)
    frameMath.grid(row = 2, column = 1, padx = 10, pady = 15)
    frameSetting.grid(row = 3, column = 1, padx = 10, pady = 5)
    frameEqual.grid(row = 3, column =2, padx = 10, pady = 5)
    frameDisclaimer.grid(row = 4, column = 1, columnspan = 2, padx = 5, pady = 2)

    calc.mainloop()

if __name__ == '__main__':
    interface()
