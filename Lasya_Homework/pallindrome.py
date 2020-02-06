# take input from user and convert string taken to all lower case
enteredString = input('Enter your string here: ').lower()

#reverse that string and compare with the input
reverseString = enteredString[::-1]

if enteredString == reverseString:
    print(enteredString,'is a palindrome')
else:
    print(enteredString, 'is not a palindrome')
