# Write a Python function to check whether a number is perfect or not. According to Wikipedia : In number theory,
# a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is,
# the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently,
# a perfect number is a number that is half the sum of all of its positive divisors (including itself). Example : The
# first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently,
# the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect
# number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

# define function to check the number is a perfect number
def Perfect_Number(Number):
    Sum = 0
    for i in range(1, Number):

        # if the given integer is perfectly divisble by i, if true add i to sum
        if Number % i == 0:
            Sum = Sum + i
    return Sum


# taking input from the user
Number = int(input("Please enter any positive integer: "))
if Number == Perfect_Number(Number):
    print(f'\n{Number} is a Perfect Number')
else:
    print(f'\n{Number} is a not a Perfect Number')