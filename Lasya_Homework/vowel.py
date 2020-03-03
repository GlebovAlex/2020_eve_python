'''
1) count the number of each vowel in a string using dictionary and list comprehension.
'''

# created a vowel list with all the vowel alphabets as elements
vowel = ['a','e','i','o','u']
vowel_Counts = dict()
userInput = input('Enter your string input here: ').lower()

'''
iterated through the user provided string char by char
if a char is a vowel then add that to a dictionary vowel_counts with vowel as key and count as value 
'''
for i in userInput:
    if i in vowel and i not in vowel_Counts:
        vowel_Counts[i] = 1
    elif i in vowel and i in vowel_Counts:
        vowel_Counts[i] +=1
print(vowel_Counts)

for alphabet,counts in vowel_Counts.items():
    print(alphabet,'is repeated',counts,'times in given string')