'''

1. Why are local variable names beginning with an underscore discouraged?

Answer: leading underscores are used to indicate variables that must not be accessed from outside the class.

2. Why lambda forms in python does not have statements?

Answer: It is mainly due to statement blocks in Python being delimited by whitespace and indentations.

'''
# 3. How can you share global variables across modules?

c = 1 # global variable
def add():
    global c # keyword "global" allows modification from anywhere
    print(c) # access global variable from inside a function
    c = c + 2 # Modifying global variable from inside a function
    print("C value after modifying is: " + str(c))
add()


# 4. How will you reverse a list in Python?

myList = [3, 6, 9, 90, 60, 30, 12, 24]
print(f'Original list is: {myList}')
myList.reverse()
print(f'Reversed list is: {myList}')