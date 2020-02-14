'''
Write a Python program to check the priority of the four operators (+, -, *, /)
'''

priority = {'+':0,'-':0,'*':1,'/':1}
operator = input('Enter the operator + or  - or * or / :: ')
print('{} is the priority of chosen operator'.format(priority[operator]))