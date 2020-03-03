'''
What is a dictionary in Python?
'''

example = {"name":"Lasya","Gender": "Female"}
#print(example)
example["name"] = "Priya"
#print(example)
example["location"] = "California"
#print(example)
example[0] = "second name"
print(example)

for i,j in example.items():
    print(i,j)