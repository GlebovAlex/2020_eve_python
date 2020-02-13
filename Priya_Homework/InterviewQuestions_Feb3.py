'''

1. What is the difference between deep and shallow copy?
Shallow Copy - new object stores the reference of another object.
Deep Copy - new object stores the reference of another object.

2. How is Multi threading achieved in Python?

3. What is the process of compilation and linking in python?

Compilation: The source code in python is saved as a .py file which is then compiled into a format known as byte code, byte code is then converted to machine code. After the compilation, the code is stored in .pyc files and is regenerated when the source is updated. This process is known as compilation.

Linking: Linking is the final phase where all the functions are linked with their definitions as the linker knows where all these functions are implemented. This process is known as linking.



4. What are Python libraries? Name a few of them.
Answer: Python library, built-in modules, is a collection of functions and methods that allows you to perform many actions without writing your code.
eg: NumPy, TensorFlow, Pandas, PyTorch

'''

# import copy
# aList = [[1,2,3], [4,5,6]]
# print(f'{aList}\n')
# aRef = copy.copy(aList) # Shallow copy
# print(f'aref after shallow copy before changing value:\n{aRef}')
# bRef = copy.deepcopy(aList) # deep copy
#
# aList[1][2] = 9
#
# print(f'Shallow Copy demonstration:\n{aList}\n{aRef}\n')


# import copy
#
# my_Var = 3
# copy_var = copy.copy(my_Var) # shallow copy
# copy_var += 2
# print(f'my_var: {my_Var}\ncopy_var: {copy_var}\n')
#
# deep_var = copy.deepcopy(my_Var) # deep copy
# deep_var += 6
# print(f'my_var: {my_Var}\ndeep_var: {deep_var}\n')