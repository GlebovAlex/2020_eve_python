# Write a Python program to find the median among three given numbers
'''
Sample Input:
[33, 24, 15]

Sample Output: 24
'''

# def a function to find median
def find_median(givenlist):

    # sort the given list
    givenlist.sort()
    print(f'Sorted input: {givenlist}')

    # find the middle number among the three numbers
    # median = givenlist[1]

    # finding median if the list has more than three elements
    if len(givenlist) % 2 == 0:
        ceilHalf = (len(givenlist) // 2)
        floorHalf = (len(givenlist) // 2) - 1
        median = float((given_list[ceilHalf] + given_list[floorHalf]) / 2)
    else:
        median = (len(givenlist) // 2)
        median = givenlist[median]

    # return the median value
    return 'Median among the three numbers is: {}'.format(median)


# get multiple inputs from user and add to the list
given_list = list(map(int, input("Enter your numbers to find median (use space): ").split()))

# get multiple inputs from user using list comprehension
# given_list = [int(given_list) for given_list in input("Enter three integers to find median: ").split()]

# call the function and pass user input as arguments to the function
print(find_median(given_list))

# import numpy
# given_list = list(map(int, input("Enter three integers to find median: ").split()))
# given_list.sort()
# print(f'Sorted input: {given_list}')
# median = numpy.median(given_list)
# print(median)