# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# You can use the else keyword to define a block of code to be executed if no errors were raised:
# The finally block, if specified, lets you execute code, regardless of the result of the try- and except blocks.

'''

Here is a simple explanation for the syntax.

try:
   You do your operations here
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block.
finally:
   Execute this block regardless of the results of other blocks.

'''

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


# You can use the else keyword to define a block of code to be executed if no errors were raised:

# This can be useful to close objects and clean up resources:

#Try to open and write to a file that is not writable:
try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()

# To throw (or raise) an exception, use the raise keyword.



x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero") # Raise an error and stop the program if x is lower than 0:


x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed") # Raise a TypeError if x is not an integer: