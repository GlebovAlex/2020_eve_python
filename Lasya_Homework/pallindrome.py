# take input from user and convert string taken to all lower case
enteredString = input('Enter your string here: ')

#reverse that string and compare with the input
def palindrome(enteredString):
    enteredString.lower()
    reverseString = enteredString[::-1]

    if enteredString == reverseString:
      return (enteredString,'is a palindrome')
    else:
        return (enteredString, 'is not a palindrome')

print(palindrome(enteredString))