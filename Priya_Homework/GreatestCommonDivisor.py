# Write a Python program to find the greatest common divisor (gcd) of two integers

def find_gcd(int1, int2):
    # check if the given numbers are positive and non zero

        if (int2 == 0):
            # return the gcd value
            return 'The Greatest common divisor of the given integers is: {}'.format(int1)
        else:
            return find_gcd(int2, int1 % int2)


print(find_gcd(12, 24))