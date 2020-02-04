'''
What is the purpose of is, not and in operators? v
'''

numbers = [1,2.0,3,4]
for i in numbers:
    if  type(i) is int:
        print(i,"is integer")
    elif type(i) is not int:
        print(i,"is not a integer")
