'''
What advantages do NumPy arrays offer over (nested) Python lists?
'''

"""
they don’t support “vectorized” operations, like elementwise addition and multiplication, 
and the fact that they can contain objects of differing types mean 
,that Python must store type information for every element, 
and must execute type-dispatching code when operating on each element

"""

'''
How to add values to a python array?
How to remove values to a python array?
'''
import numpy as np

arr = np.array([1,2,3])
print(arr)
arr = np.insert(arr,1,0)  #(array,index,value)
print(arr)
arr = np.delete(arr,1)  #(array,index)
print(arr)

'''
 4.   Does Python have OOps concepts? What it means??
'''
