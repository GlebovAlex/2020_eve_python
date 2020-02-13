'''

Make a two-player Rock-Paper-Scissors game.
Rules:
Rock beats scissors
Scissors beats paper
Paper beats rock
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

'''

input1 = input(f'Player 1, What do you want to choose: Rock, Paper, Scissors? ')
input2 = input(f'Player 2, What do you want to choose: Rock, Paper, Scissors? ')

def compare(p1, p2):
    if p1 == p2:
        return(f'Its a tie!')
    elif p1 == 'Rock':
        if p2 == 'Scissors':
            return(f'Rock wins!')
        else:
            return(f'Paper wins!')
    elif p1 == 'Scissors':
        if p2 == 'Paper':
            return(f'Scissors wins!')
        else:
            return(f'Rock wins!')
    elif p1 == 'Paper':
        if p2 == 'Rock':
            return(f'Paper wins!')
        else:
            return(f'Scissors wins!')
    else:
        return(f'Invalid Input! Please enter either of Rock, Paper or Scissors')


print(compare(input1, input2))