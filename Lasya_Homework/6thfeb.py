'''
Create a program that will play the “cows and bulls” game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
 For every digit that the user guessed correctly in the correct place, they have a “cow”.
 For every digit the user guessed correctly in the wrong place is a “bull.”
  Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
  Once the user guesses the correct number, the game is over.
  Keep track of the number of guesses the user makes throughout the game and tell the user at the end.
Say the number generated by the computer is 1038. An example interaction could look like this:
 Welcome to the Cows and Bulls Game!
 Enter a number:
 >>> 1234
 2 cows, 0 bulls
 >>> 1256
 1 cow, 1 bull
'''
import random
print('Welcome to the Cows and Bulls Game!')

# Take guessed number from user and also generate a random 4-digit number
userGuessedNumber = input('Enter a number: ')
randomNumber = str(random.randint(0,10000))
'''
following steps is just for test
'''
print('This is the random number generated ',randomNumber)
cow,bull = 0,0
cows,bulls =0,0

# getting user guessed numbers until it matches random number
while userGuessedNumber != randomNumber:
    cow, bull = 0, 0
    for indx,unum in enumerate(userGuessedNumber):
        for rindx,rnum in enumerate(randomNumber):
            if indx == rindx and unum==rnum:       #check if the digit enter by user matches with random digit including index
                cow +=1
            if indx != rindx and unum==rnum:    #check if the digit enter by user matches with random digit exclusind same index
                bull +=1
    cows = cows +cow
    bulls = bulls+bull
    print('{} Cows, {} Bulls'.format(cow,bull))
    userGuessedNumber = input('Enter a number: ')

print('In this game you got {} Cows, {} Bulls'.format(cows,bulls))