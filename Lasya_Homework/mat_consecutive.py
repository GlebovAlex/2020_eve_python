import numpy as np


def check_consecutive(lst,str):
    rowCount = 0
    for row in lst:
        rowCount +=1
        for i in range(len(row) - 2):
            if row[i] == row[i + 1]:
                if row[i] == row[i + 2]:
                    if str == 'row':
                        print('three "',row[i],'" in',str,rowCount-1)
                        return True
                    elif str == 'column':
                        print('three "',row[i],'" in',str,rowCount-1)
                        return True



a = [[0,0,1,3,4,5],[0,3,2,5,0,9],[9,7,2,5,0,9]]
print(np.array(a))

row_consecutive = check_consecutive(a,'row')
column_consecutive = check_consecutive(np.transpose(np.array(a),(1,0)),'column')

if row_consecutive is not True and column_consecutive is not True:
    print('The matrix DOES NOT contain any consequent numbers in either row or column')



