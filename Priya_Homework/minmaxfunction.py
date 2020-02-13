# What does min() and max() functions do?

# max() is used to compute maximum of the values passed in the argument and lexicographically largest value if strings are passed as arguments.

# syntax: max(a,b,c,..) where parameters are similar type of data.

print(max(4,12,33,124,50,79,80))
print(min(324,63,78,62,71,60))

# when the parameters of different data type are passed, throws a type error

print(max(4,12,33,"Python",50,79,80))

# finding lexicographically largest and smallest of Strings i.e String appearing first in dictionary or last.

print(min("Python", "is", "fun", "Priya", "enjoys", "learning", "Python"))
print(min("python", "is", "fun", "priya", "enjoys", "learning", "python"))
print(True if "priya" > "Priya" else False)