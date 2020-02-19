'''
Write a Python program to calculate the value of 'a' to the power 'b'.
'''

def powerOf(num,power):
    if power == 0:
        return 1
    elif power == 1:
        return num
    else:
        result = num # initializing result with input num
        while power > 1: # perform muliplication as long as power is > 1
            result = result * num
            power = power - 1
        return result

print(powerOf(3,40))
print(3**40)