'''
What is Polymorphism in Python?
'''

# In programming, polymorphism means same function name (but different signatures) being uses for different types.

#example: len()

def add(a,b):
    return a+b

print(add(2,3))
print(add('a','b'))

'''
Polymorphism with Inheritance:
method overide
'''


class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("birds can fly.")


class ostrich(Bird):
    def flight(self):    #func name is same as parent class
        print("Ostriches cannot fly.")

