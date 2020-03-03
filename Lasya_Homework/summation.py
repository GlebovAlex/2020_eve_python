'''
Write a Python program to compute the summation of the absolute difference of all distinct pairs in an given array
(non-decreasing order).
Sample array: [1, 2, 3]
Then all the distinct pairs will be:
1 2
1 3
2 3
'''
from itertools import combinations

arr = [1, 3, 2]
sum = 0
distinct_list=  list(combinations(arr, 2)) # getting all possible combinations, passing second arg as 2 because we need pair
print(distinct_list)

for pair in distinct_list: # looping through all the pairs in list
    sum = sum + abs(pair[1]-pair[0]) # getting absolute difference of pairs and computing sum of same

print(sum)