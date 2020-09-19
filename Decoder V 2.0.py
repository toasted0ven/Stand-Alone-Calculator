# Decoder V 2.0

# This version is to re-write the decoder so that it's workings can actually be understood.
# The changes to the first version is that each operation is called separately and then a decoding
# script is run to deal with brackets by calling itself when it encounters them passing the internal
# text as the new text to be decoded. This function then calls each operation as they are required.
# Hopefully this makes the entire process easier to de-bug, especially when the stiching process comes
# about again for calculator V 2.0

# Operating assumptions/proticols:
# - all processes completed using floats and convert to int if possible at the end




def add(x):
    # expected text is "num + num"
    mid = x.find("+")
    mid_plus = mid + 2
    mid_minus = mid - 1
    num1 = x[0 : mid_minus]
    num2 = x[mid_plus: len(x)]
    ans = float(num1) + float(num2)
    print (str(num1) + " + " + str(num2))
    print (ans)
    return ans

def minus(x):
    # expected text is "num - num"
    mid = x.find("-")
    mid_plus = mid + 2
    mid_minus = mid - 1
    num1 = x[0 : mid_minus]
    num2 = x[mid_plus: len(x)]
    ans = float(num1) - float(num2)
    print (str(num1) + " - " + str(num2))
    print (ans)
    return ans

def multiply(x):
    # expected text is "num x num"
    mid = x.find("x")
    mid_plus = mid + 2
    mid_minus = mid - 1
    num1 = x[0 : mid_minus]
    num2 = x[mid_plus: len(x)]
    ans = float(num1) * float(num2)
    print (str(num1) + " x " + str(num2))
    print (ans)
    return ans

def divide(x):
    # expected text is "num / num"
    mid = x.find("/")
    mid_plus = mid + 2
    mid_minus = mid - 1
    num1 = x[0 : mid_minus]
    num2 = x[mid_plus: len(x)]
    ans = float(num1) / float(num2)
    print (str(num1) + " / " + str(num2))
    print (ans)
    return ans



def bracket_find(text):
    # Not sure why, but I'm counting the brackets...
    tot_open = text.count("(")
    tot_close = text.count(")")

    # Trying to find a bracket set that doesn't have a bracket in it
    first_open = text.find("(")
    text_temp = text
    for i in range (0,tot_open):
        first_close = text_temp.find(")")
        text_temp = text[first_open:first_close+1]
        if text_temp.find("(") != -1:
            first_open = first_open + text_temp.find("(")
        else:
            break
    return text_temp

    

def decoder(x):
    num1 = x.count("(")
    num2 = x.count(")")
    if num1 != num2:
        #some form of error
        print("Error message informing user that the number of brackets is wrong")
    if num1 >= 1:
        first = x.find("(")
        last = x.rfind(")")
        new_x = x[first+1:last]
        print ("new x is: " + str(new_x))
        y = decoder(new_x)
        print("y is : " + str(y))
        x = x[0:first,y,last:-1]
    else:
        if x.find(" + ") != -1:
            # this will work only if there is only 1 plus and 2 numbers. need to add something that works for more
            x = add(x)
    
    return x 
        
    



# testing
#add("111 + 222")
#minus("234 - 123")
#multiply("11 x 12")
#divide("765 / 5")

# add(" - 111 + 234")
# This is a problem - essentially we need a way to have the program assign the " - num" as "-num"
# basically removing the spaces in the text.


decoder("(((11 + 11) x 10))")


