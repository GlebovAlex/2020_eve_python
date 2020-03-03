# Python Iterators
# Return an iterator from a tuple, and print each value

mytuple = ("Python", "Javascript", "Java")
myIteratn = iter(mytuple)
print(next(myIteratn))
print(next(myIteratn))

mystring = "Python"
myIteration = iter(mystring)
print(next(myIteration))

# Iteration in a for loop

myString = "Python"
for i in myString:
    print(i)


# *********************
# What does [::-1} do?
# Omitting the two index numbers and retaining colons will keep the whole string within range, while adding a final parameter for stride will specify the number of characters to skip.
# indicate a negative numeric value for the stride, which we can use to print the original string in reverse order if we set the stride to -1

sequence = "Learning Python"
print(sequence)
# print(sequence[::-1])
# print(sequence[:-2])
# print(sequence[::-2])
# print(sequence[::-3])
print(sequence[6::-2])



# **********************************
# How does break, continue and pass work?
# break statement terminates the current loop and resumes the next statement

for string in "Python":
    if string == "o":
        break
    print(string)

# continue statement skips current iteration of a loop and continues with the rest of the loop

for string in "Javascript":
    if string == "p":
        continue
    print(string)

# pass statement allows the program to handle a condition of a loop without impacting any of the iterations

for string in "Testing":
    if string == "i":
        pass
    print(string)

