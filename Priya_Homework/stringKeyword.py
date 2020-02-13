# Given a string, write a Python program that checks if the given string is keyword or not.
# Keywords are reserved words which cannot be used as variable names.
# There are 33 keywords in Python programming language.(in python 3.6.2 version)

import keyword
from keyword import kwlist

# userString = input(f'Enter a string: ')
# if keyword.iskeyword(userString):
#     print(f'"{userString}" is a Python keyword.\n')
# else:
#     print(f'"{userString}" is not a keyword.\n')
#
# print(f'Keywords in Python are: \n{kwlist}')

def stringIsKeyword(uString):
    check = keyword.kwlist
    if uString in check:
        return (f'"{uString}" is a Python Keyword\n')
    else:
        return (f'"{uString}" is not a Python Keyword\n')

print(f'Keywords in Python are: \n{kwlist}')

if __name__ == "__main__":

    userString = input(f'Enter a string: ')
    print(stringIsKeyword(userString))