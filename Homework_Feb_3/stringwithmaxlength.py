# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.

def maxStringLen(string1, string2):
    if len(string1) > len(string2):
        print("The string with maximum length is: " + string1)
    elif len(string1) < len(string2):
        print("The string with maximum length is: " + string2)
    elif len(string1) == len(string2):
        print(string1 + "\n" + string2)

userString1 = input("Enter the first string: ")
userString2 = input("Enter the second string: ")


maxStringLen(userString1, userString2)
