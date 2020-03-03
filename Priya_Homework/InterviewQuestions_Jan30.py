# How can the ternary operators be used in python?

# if statements
x, y = 3, 6
if x > y:
    print(str(x) + " is greater than " + str(y))
else:
    print(str(y) + " is greater than " + str(x))

# using ternary operators
# x, y = 3, 6
# print("x" if x > y else "y")
# print(str(x) + " is greater than " + str(y) if x > y else str(y) + " is greater than " + str(x))


# python basically first evaluates the condition, if true – evaluate the first expression else evaluates the second condition

# def greaterNumber(x,y):
#     return x if x > y else y
# print(greaterNumber(12,11))

# tuples, dictionary

# using lambda function as ternary operator

x, y = 33, 12
# # print((lambda: f"{x} is greater than {y}", lambda: f"{y} is greater than {x}")[x > y]())
print((lambda: x, y)[x > y])

# def new_func(x):
#     return (lambda y: x+y)
# t = new_func(3)
# u = new_func(2)
# print(t(3))
# print(u(3))