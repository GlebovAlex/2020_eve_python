# Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

# import string


def ispangram(string):
    # variable that has the alphabets
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # for loop checks if letters are present in the given string
    for letter in alphabet:
        if letter not in string.lower():
            return False
    return True


# taking user input
string = input(f'Enter a sentence/word: ')

# function call
if (ispangram(string) == True):
    print(f'This is a pangram!')
else:
    print((f'This is not a pangram!'))

# print(ispangram("The five boxing wizards jump quickly."))
# print(ispangram("adsdg"))
# print(ispangram("The quick brown fox jumps over the lazy dog"))