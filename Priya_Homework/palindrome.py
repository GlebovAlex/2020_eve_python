# # Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if reverse of the string is same as string. For example, “radar” is palindrome, but “radix” is not palindrome

# # function that performs string reversal
# def reverse(string):
#     string = string[::-1]
#     return string

# @reverse

import string

def palindrome(string):
    string = string.lower()
    newString = string[::-1]
    if string == newString:
        # return (f'{userInput} is a palindrome!')
        # return True
        return '{} is a palindrome'.format(userInput)
    else:
        # return False
        return '{} is not a palindrome'.format(userInput)


if __name__ == "__main__":
    userInput = input("Enter a string: ") # radar, civic, level, kayak
    print(palindrome(userInput))

# # # using recursion
#
# def reverse(string):
#     if len(string) == 0:
#         return string
#     else:
#         return reverse(string[1:]) + string[0]
#
#
# userString = input("Enter a string: ")
# rString = reverse(userString)
# print(f'Original string: {userString}')
# print(f'Reversed string: {rString}')