'''

1) What is a map function in Python?

map(function, iterables)

2) When Would You Use a List vs. a Tuple vs. a Set in Python?

Answer: When to use a dictionary:
– a logical association between a key:value pair.
– fast lookup for your data, based on a custom key.
– data is being constantly modified. Remember, dictionaries are mutable.

– Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
– Use a set if you need uniqueness for the elements.
– Use tuples when your data cannot change.
Many times, a tuple is used in combination with a dictionary, for example, a tuple might represent a key, because it’s immutable.


3) How do you execute a Python Script ?

The operating system command-line or terminal
The Python interactive mode
The IDE or text editor you like best
The file manager of your system, by double-clicking on the icon of your script

4) Name the four main types of namespaces in Python
Answer: Built-in, Global (Module), Local (Function), Enclosed (Function wrapped within a function)

'''

# def calculateSquare(n):
#   return n*n
#
# numbers = (1, 2, 3, 4)
# result = map(calculateSquare, numbers)
# print(result)
#
# # converting map object to set
# numbersSquare = set(result)
# print(numbersSquare)

# # using lambda function with map()
#
# numbers = (1, 2, 3, 4)
# result = map(lambda x: x*x, numbers)
# print(result)
#
# # converting map object to set
# numbersSquare = set(result)
# print(numbersSquare)

# Passing Multiple Iterators to map() Using Lambda
#
# num1 = [2,4,6]
# num2 = [9,6,3]
# sum = map(lambda n1, n2: n1 + n2, num1, num2)
# print(list(sum))