# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#    Suppose the following input is supplied to the program:
#    "Hello world!"
#    Then, the output should be:
#    UPPER CASE 1
#    LOWER CASE 9
#    Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

userString = input("Please enter a statement: ")
upperCount = 0
lowerCount = 0
for c in userString:
    if c.isupper():
        upperCount += 1
    elif c.islower():
        lowerCount += 1
print(f'UPPER CASE {upperCount}')
print(f'LOWER CASE {lowerCount}')