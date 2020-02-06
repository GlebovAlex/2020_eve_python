# created a dictionary with concatenated strings as key and winner word among strings as value

game = { "rockscissors":"rock" ,"scissorspaper":"scissors","paperrock":"paper",
         "scissorsrock":"rock" ,"paperscissors":"scissors","rockpaper":"paper"}

# Took input from player1 and player2 and concatenated the input strings
player1 = input('Rock, Paper, Scissors? ')
player2 = input('Rock, Paper, Scissors? ')
valueSelected = player1+player2

'''
Get the value from game dictionary using concatenated strings as key
and check which player entered the winning value
'''
try:
    if player1 == game[valueSelected]:
        print('Congratulation Player1')
    elif player2 == game[valueSelected]:
        print('Congratulation Player2')
except:
    print('Enter valid choice')