'''
Write a Python program to find the greatest common divisor (gcd) of two integers
'''

def gcd(a,b):
    if(b==0): #base case if second number is zero return first number
        return a
    else:
        return gcd(b,a%b) # if second number is not zero call func with second number and remainder
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
GCD=gcd(a,b)
print("GCD is: ",GCD)