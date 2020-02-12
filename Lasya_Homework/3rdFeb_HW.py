'''
Use Regular Expression (or another method) to solve the task: A website requires the users to input username
and password to register. Write a program to check the validity of password input by users.
   Following are the criteria for checking the password:
   1. At least 1 letter between [a-z]
   2. At least 1 number between [0-9]
   1. At least 1 letter between [A-Z]
   3. At least 1 character from [$#@]
   4. Minimum length of transaction password: 6
   5. Maximum length of transaction password: 12
   Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
   Passwords that match the criteria are to be printed, each separated by a comma.
'''
import re

def pwd_check(password):
    result = True
    x = re.findall("\D", password)
    if not (x):
        result = False
    x = re.findall("[a-z]", password)
    if not (x):
        result = False
    x = re.findall("[A-Z]", password)
    if not (x):
        result = False
    x = re.findall("[$#@]", password)
    if not (x):
        result = False
    if len(password) not in range(6,12):
        result = False
    return result

password = input('Enter password: ')
for i in password.split(','):
    if pwd_check(i):
        print(i)