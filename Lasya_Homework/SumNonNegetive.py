'''
Write a Python program to get the sum of a non-negative integer
'''

def sumdigits(num, result):
    """
    :param num: input number
    :param result: sum of digits in input number
    :return: returns result
    This function calculates the sum of all digits in a number
    """
    while num > 0:
        digit = num%10 # getting last digit of a input number
        result = result + digit # calculating sum of digits
        num = int(num / 10) # num will now have number without the digit we extracted above
    return result
print(sumdigits(53,0))