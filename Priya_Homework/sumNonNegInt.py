# Write a Python program to get the sum of a non-negative integer

# print(sum(list(map(int, input("Enter your number ")))))

# Using Recursive Function

def sumOfNonNegInt(num):
    if num == 0:
        return 0
    elif num < 0:
        return 'This is a negative integer'
    else:
        return num % 10 + sumOfNonNegInt(num // 10)


print(sumOfNonNegInt(333333))
print(sumOfNonNegInt(0))
print(sumOfNonNegInt(-22))

