'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
   Suppose the following input is supplied to the program:
   "Hello world!"
   Then, the output should be:
   UPPER CASE 1
   LOWER CASE 9
   Hints:
   In case of input data being supplied to the question, it should be assumed to be a console input.
   '''

# Getting input from console and initializing counters.
userString = input('Enter String: ')
UPPER_CASE = 0
LOWER_CASE = 0

# Iterating through entering string and checking if it is UpperCase or LowerCase
for i in userString:
    if i.isupper():
        UPPER_CASE += 1
    elif i.islower():
        LOWER_CASE += 1

print('UPPER CASE ',UPPER_CASE,'\n','LOWER CASE ',LOWER_CASE)



