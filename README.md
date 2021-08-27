# Stand Alone Calculator
#### Video Demo:  <URL HERE>
#### Description:
##### Purpose
The aim of this project was to create a stand alone functional scientific calculator using python - not using any maths modules for the more complex functions. The project uses tkinter to create a user interface that is more usable than a text based interface, but this is the only dependency.

##### Structure
The code is split in 3 scripts - *maths.py*, *decoder_iterative_V5.0.py*, and *calc_interface.py*. All the other scripts are either previous versions or testing scripts to support the main files.

*maths.py* contains only functions for various mathematical functions such as cosine, exponential (e^x) and others. These are done using mostly taylor series expansions to get a pretty close approximation of the answers.

*decoder_iterative_V5_0.py* is a series of functions designed to figure out what the user is asking and then to go and do it. It imports and calls the functions from *maths.py* as needed. This functionality can be achieved iteratively, recursively or using some form of tree structure or class. My version, as indicated in the name, is iterative. The first step in the process is to take a text input and convert it into a list which has each entry as a separate component - ie a number, operation, bracket or function. This is then passed to the decoder function. The main idea behind the decoder function is to search through the list to find the deepest bracket - which is done by finding the last open bracket as logic dictates that there cannot be a layer deeper than that (locally) and that if there is an earlier layer that is deeper, it is independent of this one. Within a set of brackets, the function calls another function to handle the order of operations until the inside is reduced to a single number. Then, a check is done on the outside of the bracket to see if there was a mathematical function to be applied to the contents of the bracket.

*calc_interface.py* imports the decoder script and tkinter and runs the interface, calling the decoder script when the user presses the equals button. The interface buttons are the only means of the code receiving input. This was so that there would be less opportunity for input to be incorrectly inputted and allow for less checking on the code side. The structure of the interface is governed by a number of frames, each of which is packed into a specific location of the window and contains the various buttons and text fields for the calculator.

The project is intended to be run from the *calc_interface.py*. 
