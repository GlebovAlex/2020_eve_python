'''
 Write a Python program to find the median among three given numbers
 '''
# take three input numbers
first_number = float(input("Input first number: "))
second_number = float(input("Input second number: "))
third_number= float(input("Input third number: "))
fourth_number= float(input("Input fourth number: "))

# append all three input numbers to a list
numbers =[]
numbers.append(first_number)
numbers.append(second_number)
numbers.append(third_number)
numbers.append(fourth_number)
#sort the list and print the median
numbers.sort()
if len(numbers) <= 3:
    print(numbers[1])
else:
    index = int(len(numbers)/2)
    median = (numbers[index-1] + numbers[index])/2
    print(median)