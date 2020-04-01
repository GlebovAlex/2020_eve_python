# check whether an n-digit integer is an Armstrong number or not (A number is called Armstrong number if it is equal to the sum of the cubes of its own digits. For example: 153 is an Armstrong number since 153 = 1*1*1 + 5*5*5 + 3*3*3).

# function block
def armstrongNum(unum):
    # initialize sum to zero
    summ = 0
    temp = unum
    while temp > 0:
        digit = temp % 10
        summ += digit ** 3
        temp //= 10
    # display result
    if unum == summ:
        return f'{unum} is an Armstrong number'
    else:
        return f'{unum} is not an Armstrong number'


# get input from user
userNum = int(input(f'Enter an integer: '))
print(armstrongNum(userNum))
