# Write a Python program to rearrange positive and negative numbers in a given array using Lambda


def Rearrange(userList):
    # returns positive numbers followed by negative numbers
    return [x for x in userList if x < 0] + [x for x in userList if x >= 0]


# function call
userInput = list(map(int, input("Enter your numbers for the list: ").split()))
# userInput = list(map(int, input("Enter your numbers to find median (use space): ").split()))
print(Rearrange(userInput))