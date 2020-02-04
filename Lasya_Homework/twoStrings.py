'''
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print al l strings line by line.
'''

def maxString(str1,str2):
    if len(str1) != len(str2):
        print(max(str1,str2))
    else:
        print(str1,'\n',str2)

str1 = input('Enetr first string: ')
str2 = input('Enetr second string: ')
maxString(str1,str2)


