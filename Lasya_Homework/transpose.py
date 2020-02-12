import numpy as np

a = [[0,1,2,3,4],[0,3,4,5,0],[0,7,8,9,9],[1,2,0,0,0]]
print(a)
b = np.transpose(np.array(a),(1,0))
print(b)
