'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right
'''

import random
# Take guessed number from user and also generate a random  number between 1 and 9
randomNumber = random.randint(1,10)
userGuessedNumber = int(input('Enter a single digit number: '))

if userGuessedNumber < randomNumber:
    print('You guessed too low')
elif userGuessedNumber > randomNumber:
    print('You guessed too high')
else:
    print('You guessed exactly right')

