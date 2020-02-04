'''
What are docstrings in Python?
'''

def power(a, b):
    """Returns arg1 raised to power arg2."""
    return a ** b

print(power.__doc__)
print(power(2,3))

'''
What should a docstring look like?

The doc string line should begin with a capital letter and end with a period.
The first line should be a short description.
If there are more lines in the documentation string, the second line should be blank, 
visually separating the summary from the rest of the description.
The following lines should be one or more paragraphs describing the object’s calling conventions, its side effects, etc.
'''
