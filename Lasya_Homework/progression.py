'''
Write a Python program to find the type of the progression (arithmetic progression/geometric progression)
and the next successive member of a given three successive members of a sequence.
'''

def progression(sequence):
    # checking if the difference between two successive pairs is same
    if sequence[1]-sequence[0] == sequence[2]-sequence[1]:
        print('This is an arithmetic progression')
        sequence.append(sequence[2]+(sequence[2]-sequence[1]))
    # checking if there is a  common ratio between two successive pairs
    elif sequence[1]//sequence[0] == sequence[2]//sequence[1]:
        print('This is an geometric progression')
        sequence.append(sequence[2]*(sequence[2]//sequence[1]))
    else:
        print('This is neither arithmetic progression nor geometric progression')
    return sequence

user_sequence = [3, 6, 18]
print(progression(user_sequence))
