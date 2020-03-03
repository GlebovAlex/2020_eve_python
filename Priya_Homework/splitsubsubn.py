# Python has a built-in package called re, which can be used to work with Regular Expressions

import re
string = "This is Python Tutorial"
splitString = re.split("", string)
print("The split string is: " + str(splitString))
replacedString = re.sub("Py", "9", string)
replacedString = re.sub("is", "3", string, 1)# Replace the first 2 occurrences
print("The replaced string is: " + str(replacedString))

# subn() does the same as sub() except it returns a tuple with count of total of all replacements as well as the new string.
# Syntax: re.subn (pattern, repl, string, count=0, flags=0)
import re
userString = "Python's email id is pythonis@python.com"
subnString = re.subn("is", "*", userString, count = 2, flags = re.IGNORECASE)
print(subnString)
print(len(subnString))
print(subnString[0])