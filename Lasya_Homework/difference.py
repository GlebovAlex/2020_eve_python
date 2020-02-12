'''
Write a program that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.
'''

def uniqueList(lst):
    uniqueLst =[]
    for i in lst:
        if i not in uniqueLst:
            uniqueLst.append(i)
    return uniqueLst

lst = [1,2,3,4,5,6,7,2,3,4,5,6,7,1]
print(uniqueList(lst))