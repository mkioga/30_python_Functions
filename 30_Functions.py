
# =================================
# Functions
# =================================

# Functions is where you write a block of code once and then get to call and use it later without rewriting it.

# in the previous calculator code, you cannot get the calculator to calculate
# anything until we understand how to write our own functions in python.
# We have been using functions in the course so far, but we will now learn how they work
# and how we can create functions ourselves.

# In python, functions are created by the word "def" followed by the function name and parenthesis
# Because the function introduces a block of code, the "def" statement must be followed by a colon

# we will define a function called python_food

def python_food():
    print("Spam and Eggs")  # the function prints "spam and eggs". Code indented here is part of function "python_food"

# Now we can call the function "python_food() and when we run it, it prints "Spam and Eggs"

python_food()

print("="*40)


# All python functions return a result
# If you don't tell a function what to return, it will return "None"
# in our case, our function python_food() returns "None" because we did not define a paramenter to tell it what to return
# NOTE that it also runs the function to print "Spam and Eggs" and then prints "None"

# This result shows what happens when you use a function (python_food) as an argument to another function (print())
# the function (python_food) is executed and the result (None) is used as an Argument passed on to print function

print(python_food())
print("Result of function python_food is: {}".format(python_food()))

print("="*40)

# We will make the function more complicated

def python_food():
    screen_width = 80
    text = "Spam and Eggs"
    left_margin = (screen_width - len(text)) // 2  # left_margin is (screen_width - length of text ) / 2
    right_margin = left_margin
    print("=" * left_margin, text, "=" * right_margin)  # We print "=" x left_margin, text, and "=" x right margin

# Now we call the function python_food and it prints the text surrounded by the "==="

python_food()         # Calls the function
print(python_food())  # Calls the function and then Returns None

print("="*40)

# =====================================
# Passing an argument to function
# =====================================

# Now we will pass an argument to function

def python_food(text): # We define funtion and indicate we will pass it parameter named "text"
    screen_width = 80
    left_margin = (screen_width - len(text)) // 2  # left_margin is (screen_width - length of "text" ) / 2
    right_margin = left_margin
    print("=" * left_margin, text, "=" * right_margin)  # Note that we include "text" here to print

# Now we call the function python_food and pass it parameters in the ()
# so when it prints, it replaces "text" with the parameter we pass it in the position where (text) was
# Here we call the function "python_food()" and pass different parameters to it.

python_food("Spam and Eggs")
python_food("Spam, Spam and Eggs")
python_food("Spam, Spam, Spam, Spam and Eggs")

print("="*40)

# Definitions
# "Aarameter" refers to the variable defined in the function definition e.g. in def python_food(text),
#  "text" is the parameter.

# "Argument" is the actual values passed to the function when it is called e.g. in python_food("Spam and Eggs)",
# "Spam and Eggs" are the Arguments

# NOTE that "parameter" and "argument" are sometimes used interchangeably


# ==========================================
# In above code, if you pass it an integer as argument, you get an error as shown below
# The cause is because in line "len(text)" the "len" function only pulls length for strings.
# Hence if you pass it an integer, it will not work.
# The solution here is you can add line "text = str(text)" to convert any argument passed to string

def python_food(text): # We define funtion and indicate we will pass it parameter named "text"
    screen_width = 80
    text = str(text)  # Converts any argument, including integer to text.
    left_margin = (screen_width - len(text)) // 2  # left_margin is (screen_width - length of "text" ) / 2
    right_margin = left_margin
    print("=" * left_margin, text, "=" * right_margin)  # Note that we include "text" here to print


python_food("Spam and Eggs")
python_food("Spam, Spam and Eggs")
python_food(12)

print("="*40)

# ===============================================================
# print function
# ===============================================================

# if you CTRL+click print function, you will see its definition as follows
# def print(self, *args, sep=' ', end='\n', file=None)
# the *args, means that print function can take many arguments in the same line
# this is why we are able to pass print() with many arguments below and it will print them

print("First", "Second", 3, 4, "spam")
print()

print("="*40)

# ============================================================================
# We can add the functionality of taking multiple arguments to our function "center_text" below
# NOTE: we just replaced function name "python_food" with "center_text"
# =============================================================================


def center_text(*args): # We define funtion to take many arguments (*args)
    text = ""  # We initialize text to have nothing

    # This for loop will pull the different arguments we give it one by one.
    # Then replace the text with "string" format of the argument and add a space " " between them

    for arg in args:
        text += str(arg) + " "

    left_margin = (80 - len(text)) // 2  # left_margin is (screen_width (80 in this case) - length of "text" ) / 2
    right_margin = left_margin
    print("=" * left_margin, text, "=" * right_margin)  # Note that we include "text" here to print


center_text("Spam and Eggs")
center_text("Spam, Spam and Eggs")
center_text(12)
center_text("first", "second", 3, 4, "spam")

print("="*40)

# NOTE that while above method works, it is not the most efficient way to do things when passing multiple arguments
# Later we will look into "List Comprehension" method



# ========================================================
# Adding named parameters to our function center_text()
# ========================================================

# When you CTRL+click on print() function, you see definitions below
# we will now add the other named parameters (sep, end, file) to our center_text function

# def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
#     """
#     print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
#
#     Prints the values to a stream, or to sys.stdout by default.
#     Optional keyword arguments:
#     file:  a file-like object (stream); defaults to the current sys.stdout.
#     sep:   string inserted between values, default a space.
#     end:   string appended after the last value, default a newline.
#     flush: whether to forcibly flush the stream.
#     """


def center_text(*args, sep=' ', end='\n', file=None, flush=False): # Add named arguments with defaults. But we can pass something different when calling function
    text = ""  # We initialize text to have nothing

    # This for loop will pull the different arguments we give it one by one.
    # Then replace the text with "string" format of the argument and add a space " " between them

    for arg in args:
        text += str(arg) + sep  # instead of adding " ", we add sep which gives default separator of ' '

    left_margin = (80 - len(text)) // 2  # left_margin is (screen_width (80 in this case) - length of "text" ) / 2
    right_margin = left_margin
    print("=" * left_margin, text, "=" * right_margin, end=end, file=file, flush=flush)  # end=end refers to end in center_text above, same for file and flush


center_text("Spam and Eggs")  # First three lines, sep is default ' '
center_text("Spam, Spam and Eggs")
center_text(12)
center_text("first", "second", 3, 4, "spam", sep=":")  # here we pass sep argument as : and see results separated by :

print("="*40)

# =====================================================
# NOTE that we used naming "sep=' ', end='\n', file=None, flush=False" to make it similar to print function
# But you can use whatever names you want as long as you use same ones when you call them
# We change naming to : sep_char=' ',end_char='\n', file_centered=None, flush_file=False)

# These names that can be changed but referring to same thing are called "signature".
# "Signature" refers to a set of parameters in a function definition.
# Two functions that take the same parameters are said to have the same signature.

# it is however advisable to use same names as the print function


def center_text(*args, sep_char=' ', end_char='\n', file_centered=None, flush_file=False): # using different naming
    text = ""  # We initialize text to have nothing

    # This for loop will pull the different arguments we give it one by one.
    # Then replace the text with "string" format of the argument and add a space " " between them

    for arg in args:
        text += str(arg) + sep_char  # use sep_char here which we defined above as '\n'

    left_margin = (80 - len(text)) // 2  # left_margin is (screen_width (80 in this case) - length of "text" ) / 2
    right_margin = left_margin
    print("=" * left_margin, text, "=" * right_margin, end=end_char, file=file_centered, flush=flush_file)  # We add the named parameters in print


center_text("Spam and Eggs")  # First three lines, sep is default ' '
center_text("Spam, Spam and Eggs")
center_text(12)
center_text("first", "second", 3, 4, "spam", sep_char=":")  # Also make sure to replace with sep_char here

print("="*40)


# ==================================================
# How to make output go to a file
# ==================================================

# In this case, we will send the output to a file named "centered"
# This will appear on the left side after we run the code.
# When you click on the "centered" file on the left, it has all the info that should have been printed.

def center_text(*args, sep=' ', end='\n', file=None, flush=False): # We add all the named arguments here
    text = ""  # We initialize text to have nothing

    # This for loop will pull the different arguments we give it one by one.
    # Then replace the text with "string" format of the argument and add a space " " between them

    for arg in args:
        text += str(arg) + sep  # instead of adding " ", we add sep which gives default separator of ' '

    left_margin = (80 - len(text)) // 2  # left_margin is (screen_width (80 in this case) - length of "text" ) / 2
    right_margin = left_margin
    print("=" * left_margin, text, "=" * right_margin, end=end, file=file, flush=flush)  # We add the named parameters in print

with open("centered", mode="w") as centered_file:

    center_text("Spam and Eggs", file=centered_file)  # this will go to centered_file instead of default "None"
    center_text("Spam, Spam and Eggs", file=centered_file)
    center_text(12, file=centered_file)
    center_text("first", "second", 3, 4, "spam", sep=":", file=centered_file)

print("="*40)


# ==========================================
# using the "return" method
# ==========================================

# when using "return" method below, the results after "return" are returned to the function "center_text"
# then when function "center_text" is called, the returned "left_margin and right_margin" are concantenated
# with the "argument" passed e.g. "Spam and Eggs" and then printed


def center_text(*args, sep=' '): # We add only arguments we are using
    text = ""  # We initialize text to have nothing
    for arg in args:
        text += str(arg) + sep  # instead of adding " ", we add sep which gives default separator of ' '
    left_margin = (80 - len(text)) // 2  # left_margin is (screen_width (80 in this case) - length of "text" ) / 2
    right_margin = left_margin
    return "=" * left_margin + text + "=" * right_margin  # Returns result to the center_text function

# Print function prints the "argument and concantenates it with the left_margin and right_margin returned above.

print(center_text("Spam and Eggs"))  #
print(center_text("Spam, Spam and Eggs"))
print(center_text(12))
print(center_text("first", "second", 3, 4, "spam", sep=":"))

print("="*40)

# you can get similar results by assigning the results of return to a variable, then printing the variable

def center_text(*args, sep=' '): # We add only arguments we are using
    text = ""  # We initialize text to have nothing
    for arg in args:
        text += str(arg) + sep  # instead of adding " ", we add sep which gives default separator of ' '
    left_margin = (80 - len(text)) // 2  # left_margin is (screen_width (80 in this case) - length of "text" ) / 2
    right_margin = left_margin
    return "=" * left_margin + text + "=" * right_margin  # Returns result her to the center_text function

# assign result to variables

s1 = center_text("Spam and Eggs")
s2 = center_text("Spam, Spam and Eggs")
s3 = center_text(12)
s4 = center_text("first", "second", 3, 4, "spam", sep=":")

# Then print the variable

print(s1)
print(s2)
print(s3)
print(s4)

print("="*40)


# ============================================================
# You can send the results into a file named "menu_file"
# ============================================================


def center_text(*args, sep=' '): # We add only arguments we are using
    text = ""  # We initialize text to have nothing
    for arg in args:
        text += str(arg) + sep  # instead of adding " ", we add sep which gives default separator of ' '
    left_margin = (80 - len(text)) // 2  # left_margin is (screen_width (80 in this case) - length of "text" ) / 2
    right_margin = left_margin
    return "=" * left_margin + text + "=" * right_margin  # Returns result her to the center_text function


with open("menu_file", "w") as menu_file:  # open and use parameter "w" to write to menu_file

    # assign result to variables
    s1 = center_text("Spam and Eggs")
    s2 = center_text("Spam, Spam and Eggs")

    # send to file named "menu_file"
    print(s1, file=menu_file)
    print(s2, file=menu_file)

    # You can send these into "menu_file" directly
    print(center_text(12), file=menu_file)
    print(center_text("first", "second", 3, 4, "spam", sep=":"), file=menu_file)


