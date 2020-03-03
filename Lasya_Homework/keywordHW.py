'''
Given a string, write a Python program that checks if the given string is keyword or not.
Keywords are reserved words which cannot be used as variable names.
There are 33 keywords in Python programming language.(in python 3.6.2 version)
'''

# importing module keyword which has all python keywords as list in kwlist
import keyword
keyList = keyword.kwlist
userWord = input('Enter a word: ')

# checking if  user entered word is in keyword list
if userWord in keyList:
    print('The given string is keyword')
else:
    print('The given string is NOT a keyword')