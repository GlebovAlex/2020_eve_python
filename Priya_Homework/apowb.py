# Write a Python program to calculate the value of 'a' to the power 'b'.

def apowb(a, b):
    if a and b > 0:
        return a ** b
    else:
        return 'Enter non zero numbers!'

uInput1 = int(input('Enter first number: '))
uInput2 = int(input('Enter second number: '))
print(apowb(uInput1, uInput2))
