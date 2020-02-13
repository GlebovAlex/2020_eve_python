# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right

# import random
#
# randomNumber = int(input(f'Enter a number between 1 and 9: '))
# number = random.randint(1,10)
# if randomNumber == number:
#     print(f'Congratulations! You guessed it right.')
# elif randomNumber > number:
#     print(f'You guessed too high!')
# elif randomNumber < number:
#     print(f'You guessed too low!')


# Write a program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.


# userInput = input(f'Please give a list: ')
# userList = (userInput.split())
# userList = [3,6,9,12,10,3,6,9]
# newList = []
# for num in userList:
#     if num not in newList:
#         newList.append(num)
# print(newList)

# using a function
#
# def listElements(userList):
#     newList = []
#     for num in userList:
#         if num not in newList:
#             newList.append(num)
#     return newList
#
# userInput = input(f'Please give a list: ')
# userList = (userInput.split())
# print(listElements(userList))

using list comprehension
userList = [3,6,9,12,10,3,6,9]
newList = []
newList = [num for i, num in enumerate(userList) if num not in newList[:1]]
print(newList)

# from _collections_abc import dict_keys
# uList = [3,6,9,12,10,3,6,9]
# print(list(dict.fromkeys(uList)))

# listA = [1,2,3]
# squareList = [a**2 for a in listA]
# print(squareList)