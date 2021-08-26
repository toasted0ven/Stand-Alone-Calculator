'''
Author: Andrew Close
Date: 26/08/2021
Description:
This script deals with interpreting the user input and resolving it into the
mathematical commands that need to be completed to output the final answer.
The main functions are the text to list function which translates the text input
into a list of individual components, and the decoder which takes that list and
using order of operations logic determines the order in which to complete the
tasks.

overview:
inherited functions from previous versions:
list_search_r - reverse list search used for finding brackets
list_search - similar to index method but allows a later starting point
text_to_list - is the conversion from the raw input to a list
call_fun - deals with a fuction and a number - sin(x) for example

Either very recent or written for this version:
do_simple_maths - deals with most of bedmas operations, but not order of ops
order_of_ops - calls relevant do_simple_maths based on order of ops
run_an_op - impliments each level of the order of ops - helper to order_of_ops
decoder - deals with brackets, calling functions and calling order of ops
'''

from maths import *

def decoder(list_x, angle_setting='rad'):
    # here we could be given anything. First task is to check for brackets

    # bracket balance
    num_open = list_x.count('(')
    num_closed = list_x.count(')')
    number = False
    if num_open != num_closed:
        print('there is an unequal number of open and close brackets')
        return False
    if num_open == 0:
        # silly correction - the while loop won't run if the input doesn't have brackets - almost needs a do-while
        num_open = 1
    while num_open > 0:
        # this needs to take the number of brackets down each loop
        # we need to go into the inner most bracket - this is done by going to the last open bracket and the next closed one
        # then we need to check whats in the bracket - ie is it one or more terms and are they simple or not
        # also we need to check whats outside the - if there is like a function such as sin or cos
        # I think we can assume that the functions can only work with brackets involved
        num_open = list_x.count('(')
        last_open, last_open_checker = list_search_r(list_x, '(')
        next_close = list_search(list_x, ')', last_open)
        if last_open_checker:
            mini_list = list_x[last_open + 1:next_close] # this is everything inside the brackets
        else:
            mini_list = list_x
        if len(mini_list) == 0:
            # error case - list has () in input, this will come out valid but won't do anything
            number = False #flagging to the program later that there wasn't anything here
            list_x.pop(last_open)
            list_x.pop(last_open)
        elif len(mini_list) == 1:
            # there is just a number inside the brackets
            try:
                number = float(mini_list[0])
            except ValueError:
                print('error, could not convert to float')
                return False
        else:
            # if we are inside a bracket, then there can only be simple maths
            number = order_of_ops(mini_list)
            try:
                number = float(number[0])
            except ValueError:
                print('error, could not convert to float')
                return False
            # we need to erase the rest of the mini_list from the main list
            if last_open_checker:
                for i in range(last_open + 2, next_close):
                    list_x.pop(last_open + 2) # the list will shrink such that this is the one we want to pop each time
                list_x[last_open + 1] = number
            else: # there was only simple maths in the whole thing
                list_x = [number]
        if last_open_checker:
            list_x.pop(last_open)
            list_x.pop(last_open + 1)
        # we now have number - which should just be a single float or false
        if number:
            function = False
            if last_open != 0: # check that the bracket we are investigating is not at the start
                function = list_x[last_open - 1]
                if function in func_list:
                    number = call_fun(function, number, angle_setting)
                    list_x.pop(last_open - 1) # remove the function
                else:
                    function = False
            if function:
                list_x[last_open - 1] = number  # this is because the function shifts the location by 1
            else:
                list_x[last_open] = number            
    return number

            
def order_of_ops(list_x):
    # we start here with a list that contains not brackets - only arithmatic
    for i in ['^', ['x', '/'], ['+', '-']]:
        list_x = run_an_op(i, list_x)
    return list_x


def run_an_op(symbol, list_x):
    if len(symbol) == 2:
        while True:
            if symbol[0] not in list_x and symbol[1] not in list_x:
                break
            else:
                # we need to find the first instance of either and then do the first one
                try:
                    index1 = list_x.index(symbol[0])
                except ValueError:
                    index1 = False
                try:
                    index2 = list_x.index(symbol[1])
                except ValueError:
                    index2 = False
                if index1 and index2:
                    index = min(index1, index2)
                elif index1:
                    index = index1
                elif index2:
                    index = index2
                else:
                    print('an error has occured in run_an_op function')
                    return False
                num1 = float(list_x[index-1])
                num2 = float(list_x[index+1])
                ans = do_simple_maths(num1, num2, list_x[index])
                list_x[index] = ans
                list_x.pop(index-1)
                list_x.pop(index) #this will be equiv of index +1 after the other pop command           
    else:
        while True:
            
            #Check if we need to break
            if symbol not in list_x:
                break
            else:
                index = list_x.index(symbol)
                num1 = float(list_x[index-1])
                num2 = float(list_x[index+1])
                ans = do_simple_maths(num1, num2, symbol)
                list_x[index] = ans
                list_x.pop(index-1)
                list_x.pop(index)#this will be equiv of index +1 after the other pop command
    return list_x


def call_fun(func, x, angle_setting):
    if func in ['sin', 'cos', 'tan']:
        if angle_setting == 'deg':
            x = deg_to_rad(x)
    if func == func_list[0]:
        # sin
        ans = sin(x)
    elif func == func_list[1]:
        # cos
        ans = cos(x)
    elif func == func_list[2]:
        # tan
        return tan(x)
    elif func == func_list[3]:
        # asin
        ans = arcsin(x)
    elif func == func_list[4]:
        # acos
        ans = arccos(x)
    elif func == func_list[5]:
        # atan
        ans = arctan(x)
    elif func == func_list[6]:
        # factorial
        ans = factorial(x)
    elif func == func_list[7]:
        # exp
        ans = exp(x)
    elif func == func_list[8]:
        # sqrt
        ans = sqrt(x)
    elif func == func_list[9]:
        # abs
        ans = absolute(x)
    elif func == func_list[10]:
        # ln
        ans = ln(x)
    elif func == func_list[11]:
        # log
        return log(10, x) # currently no implementation for the base, default to 10
    else:
        ans = False
    if func in ['asin', 'acos', 'atan']:
        if angle_setting == 'deg':
            # we need to convert the answer back to degrees from radians
            ans = rad_to_deg(ans)        
    return ans


def do_simple_maths(a, b, operator):
    # note this function does not care about order of ops
    if operator == operands[0]:
        return a**b
    elif operator == operands[1]:
        return a * b
    elif operator == operands[2]:
        return a/b
    elif operator == operands[3]:
        return a + b
    elif operator == operands[4]:
        return a - b
    else:
        return False


def list_search_r(a, match):
    # small module to search a list for a match from the end to the front
    for i in range(len(a) - 1, -1, -1):
        if a[i] == match:
            return i, True
    return False, False


def list_search(a, match, start=0):
    # this is a forward list search function aiming to find the closed bracket to match the last open one
    for i in range(start, len(a)):
        if a[i] == match:
            return i
    return False


def text_to_list(text):
    # Initialise the list
    new_list = []
    # text_count is to keep track of where we are in the text
    text_count = 0
    while True:
        if text[text_count] == "(" or text[text_count] == ")":
            new_list.append(text[text_count])
            text_count += 1
        else:
            # Find the next space or bracket. The plus 1 is to ensure its the next one, not the current one
            next_space = text.find(" ", text_count + 1)
            next_open_bracket = text.find("(", text_count + 1)
            next_close_bracket = text.find(")", text_count + 1)
            # This is to stop an error where there is no next space or bracket and the value assigned is -1, which
            # of course, this the min of the three numbers
            if next_space == -1:
                next_space = 10000
            if next_open_bracket == -1:
                next_open_bracket = 10000
            if next_close_bracket == -1:
                next_close_bracket = 10000
            next_break = min(next_space, next_open_bracket, next_close_bracket)
            # This checks that my crude method to fix that bug didn't go wrong
            if next_break == 10000:
                # In case the reason there aren't any more spaces or brackets is that the last thing is a number, append it
                new_list.append(text[text_count:])
                break
            # Adds new entry to the list and updates the count
            new_list.append(text[text_count:next_break])
            text_count = next_break
        # If we find ourselves at the end of the text, it would be a good idea to stop
        if text_count == len(text):
            break
    # Looking at getting rid of the spaces in the list. Hopefully it can only have spaces either side of a number or operation
    # var mark is to mark out the positions in the list that have only spaces and gets rid of them after. This is
    # because the .pop function messes with the length of the list which the for loop isn't updated to account for
    mark = []
    for i in range(len(new_list)):
        if new_list[i].find(" ") != -1:
            # If it's just the space
            if len(new_list[i]) == 1:
                mark.append(i)
                # If it's a space at the start
            elif new_list[i].find(" ") == 0:
                new_list[i] = new_list[i][1:]
    for i in range(len(mark)):
        new_list.pop(mark[i])
    return new_list


# this list is so that the code can search the item prior to the brackets to check if it should run a function
func_list = ["sin", "cos", "tan", "asin", "acos", "atan", "fact", "exp", "SQRT", "abs", "ln", "log"]
operands = ['^', 'x', '/', '+', '-']

# testing zone - will only run if this is the script that is run, not imported
test = {
    'do_simple_maths': False,
    'run_an_op': False,
    'order_of_ops': False,
    'call_fun': False,
    'decoder': True,
    'list_search': False,
    'call_fun': False
        }

def testing(test):
        
    # testing do simple maths
    if test['do_simple_maths']:
        print('testing do_simple_maths')
        print('5 + 5 = ' + str(do_simple_maths(5, 5, '+')))
        print('5 ^ 5 = ' + str(do_simple_maths(5, 5, '^')))
        print('5 - 5 = ' + str(do_simple_maths(5, 5, '-')))
        print('5 x 5 = ' + str(do_simple_maths(5, 5, 'x')))
        print('5 / 5 = ' + str(do_simple_maths(5, 5, '/')))

    # testing run_an_op
    if test['run_an_op']:
        print('testing run_an_op')
        print('5 + 5 = ' + str(run_an_op(['+', '-'], ['5', '+', '5'])))
        print('5 ^ 2 = ' + str(run_an_op('^', ['5', '^', '2'])))
        print('5 - 2 = ' + str(run_an_op(['+', '-'], ['5', '-', '2'])))
        print('5 x 2 = ' + str(run_an_op(['x', '/'], ['5', 'x', '2'])))
        print('5 / 2 = ' + str(run_an_op(['x', '/'], ['5', '/', '2'])))
        print('5 / 2 x 3 = ' + str(run_an_op(['x', '/'], ['5', '/', '2', 'x', '3'])))
        print('5 + 2 + 2 + 2 = ' + str(run_an_op(['+', '-'], ['5', '+', '2', '+', '2', '+', '2'])))

    # testing order of ops
    if test['order_of_ops']:
        print('testing order_of_ops')
        print('5 + 5 = ' + str(order_of_ops(['5', '+', '5'])))
        print('5 + 5 + 5 + 5 + 5 = ' + str(order_of_ops(['5', '+', '5', '+', '5', '+', '5', '+', '5'])))
        print('5 - 5 + 5 - 5 + 5 = ' + str(order_of_ops(['5', '-', '5', '+', '5', '-', '5', '+', '5'])))
        print('5 ^ 2 - 5 x 5 = ' + str(order_of_ops(['5', '^', '2', '-', '5', 'x', '5'])))

    # testing call_fun
    if test['call_fun']:
        print('testing call_fun')

    # testing list_search
    if test['list_search']:
        print('testing list_search')
        print('finding the index of c in [a, b, c] ' + str(list_search(['a', 'b', 'c'], 'c')))
        print('finding the index of 5 in [5, 3, 5, 1, 5] with start set to 3 ' + str(list_search([5, 3, 5, 1, 5], 5, 3)))
        print('finding the index of 5 in [6, 2, 1] ' + str(list_search([6, 2, 1], 5)))

    # testing decoder
    if test['decoder']:
        print('testing decoder')
        print('calling decoder([5 + 5]) ' + str(decoder(['5', '+', '5'])))
        print('(5 x (6 - 2 x 2)) = 10 - Check: ' + str(decoder(['(', '5', 'x', '(', '6', '-', '2', 'x', '2', ')', ')'])))
        print('sin(30) = 0.5 - Check: ' + str(decoder(['sin', '(', '0.523599', ')'])))
        print('7^2 = 49 Check: ' + str(decoder(['7', '^', '2'])))
        print('removing brackets check ' + str(decoder(['(', '(', '(', '3', ')', ')', ')'])))
        print("running test 35 " + str(decoder(['(', '(', '5', 'x', '7', ')', ')'])))
        print('running test 14 ' + str(decoder(['(', '(', '5', '-', '1', ')', 'x', '(', '6', '+', '1', ')', ')', '/', '(', '1', '+', '1', ')'])))

    # Testing call_fun
    if test['call_fun']:
        print('testing call_fun')
        print('testing sin(pi/2) (should be 1) ' + str(call_fun('sin', 1.57079632679)))
        print('testing sin(pi/6) (should be 0.5) ' + str(call_fun('sin', 0.523599)))


if __name__ == '__main__':
    testing(test)

