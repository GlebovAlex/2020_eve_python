# Count the number of each vowel in a string using dictionary and list comprehension.

def vowelCount(ustring):

    # using list comprehension
    count = {x: sum(x.count(y) for y in 'aeiou') for x in ustring.split()}

    # printing output
    return count


# get input from user
userString = input("Enter your string: ").lower()
# calling function
print(vowelCount(userString))
