from pkg_resources import *
print(dir()) # imports and prints all contents from pkg_resources package

# How can files be deleted in Python?

myFile = open("test.py")
print(myFile.read())

import os
# os.remove("test.py")# deletes the specified file
# os.rmdir("myfolder")# deletes the specified folder

if os.path.exists("test.py"):
    # print("The file exists")
    os.remove("test.py")
    # print("The file is deleted")
else:
    print("The file does not exist")


myFile = open("test.py", "w") # create a new file which doesn't exists
myFile.write("Create a new file to learn file handling in Python!") # write new content
myFile.close()
myFile = open("test.py", "r") # opens and reads the content of the file
print(myFile.read()) # prints the contents to console

# What are the built-in types of python?

from types import *
print(dir())