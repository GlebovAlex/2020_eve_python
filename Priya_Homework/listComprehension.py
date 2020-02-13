#  Count the number of each vowel in a string using dictionary and list comprehension.

# myList = input(f'Enter a string: ').lower()
# vowel = ['a', 'e', 'i' 'o', 'u']
#
# def vowelCount():
#     count = 0
#     for vowel in myList:


myList = input("Enter a string: ").lower()
vowelCount = {x:sum(1 for char in myList if char == x) for x in 'aeiou'}
print(vowelCount)