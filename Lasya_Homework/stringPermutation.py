'''
Write a Python program to get all possible two digit letter combinations from a digit (1 to 9) string.
string_maps = {"1": "abc","2": "def","3": "ghi","4": "jkl","5": "mno","6": "pqrs","7": "tuv","8": "wxy","9": "z"}
'''
from itertools import permutations

string_maps = {"1": "abc","2": "def","3": "ghi","4": "jkl","5": "mno","6": "pqrs","7": "tuv","8": "wxy","9": "z"}

def perm(num1,num2):
    str1 = string_maps[num1]
    str2 = string_maps[num2]
    for i in list(str1):
       for j in list(str2):
           print('{}{}'.format(i,j))

num1 = input('Enter first digit: ')
num2 = input('Enter second digit: ')
perm(num1,num2)