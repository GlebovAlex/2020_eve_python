# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically


def hyphensort(string):
    # using list comprehension, the user input is stored in a list after sperating them with hyphen
    ulist = [x for x in string.split('-')]
    ulist.sort()  # the list sorted
    return ('-'.join(ulist))  # then the sequence is again separated by hyphen


# taking user input and converting it to lower case
string = input(f'Enter a hyphen separated sequence of words: ').lower()
# function call
print(hyphensort(string))
# California-SAN DIEGO-america-Zimbawe-Mauritius
