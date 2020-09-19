## Attempt at non-recursive decoder ##

def main(list_x):
    # Main function for decoding the input.
    # Input: list
    # Output: Answer or error
    while True:
        print("The current list length is " + str(len(list_x)))
        last_open = list_search_r(list_x, "(") # this is the last open bracket position
        print("The first last open bracket  is "  + str(last_open))
        next_closed = list_search(list_x,")",last_open) # this is the next closed bracket position
        print("The next closed bracket is " + str(next_closed))
        mini_list = list_x[last_open+1:next_closed]
        print (mini_list) # this creates another list with only the contents of the bracket
        # Checking for a function outside the brackets
        for i in func_list:
            if i == list_x(last_open-1):
                print ("theres a function outside this thing")
                func = i
            else:
                print ("there isn't a function outside this thing")
                func = False # this gives an easy check later
        # inside the mini list we need to find all multiplication and divisions and run them, then find the addition and subtraction and run them. Then at the end, it will just need to
        # either run a function or just leave it. It might be worth having an iferror block here to try and get a single number and skip the bedmas if its just a number
        #try

        break


def list_search_r(a, match):
    # small module to search a list for a match from the end to the front
    for i in range(len(a) - 1, 0, -1):
        if a[i] == match:
            return i
    return "error"


def list_search(a, match, start):
    # this is a forward list search function aiming to find the closed bracket to match the last open one
    for i in range(start, len(a) + 1):
        #print("list index " + str(i))
        if a[i] == match:
            #print("Match at index " + str(i))
            return i
    return "error"


def text_to_list(text):
    # Initialise the list
    new_list = []
    # text_count is to keep track of where we are in the text
    text_count = 0
    while True:
        if text[text_count] == "(" or text[text_count] == ")":
            new_list.append(text[text_count])
            text_count += 1
            # print (new_list)
            # print (text_count)
        else:
            # Find the next space or bracket. The plus 1 is to ensure its the next one, not the current one
            next_space = text.find(" ", text_count + 1)
            next_open_bracket = text.find("(", text_count + 1)
            next_close_bracket = text.find(")", text_count + 1)
            # print ("next space: " + str(next_space) + "\nnext open bracket: " + str(next_open_bracket) + "\nnext closed bracket: " + str(next_close_bracket))
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
                # print ("Something probably went wrong")
                # In case the reason there aren't any more spaces or brackets is that the last thing is a number, append it
                new_list.append(text[text_count:])
                break
            # print (next_break)
            # Adds new entry to the list and updates the count
            new_list.append(text[text_count:next_break])
            text_count = next_break
            # print(new_list)
            # print(text_count)
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
                # print ("check point")
                new_list[i] = new_list[i][1:]
    for i in range(len(mark)):
        new_list.pop(mark[i])
    # print (new_list)
    return new_list


def text_to_list2(text):
    # This doesn't actually work, it doesn't do the thing for the brackets.
    text = text.split(" ")
    return text

# this list is so that the code can search the item prior to the brackets to check if it should run a function
func_list = ["sin", "cos", "tan", "exp", "atan"]

text = "(1 + 4) x (10)"
sdfak = text_to_list(text)
print(sdfak)
main(sdfak)

