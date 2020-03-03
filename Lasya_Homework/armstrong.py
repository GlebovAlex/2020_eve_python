'''
 2) check whether an n-digit integer is an Armstrong number or not
  (A number is called Armstrong number if it is equal to the sum of the cubes of its own digits.
   For example: 153 is an Armstrong number since 153 = 1*1*1 + 5*5*5 + 3*3*3).
'''

def armstrong(num):
    #  get n power of all the digits in entered number with n-digits and add it
    sum =0
    for i in num:
        power = int(i) ** len(num)
        sum = sum + power
# check if the entered number is armstrong by comparing with te sum calculated above
    if sum == int(num):
        print(num,'is an Armstrong number')
    else:
        print(num, 'is NOT an Armstrong number')

armstrong(input('Enter an integer: '))