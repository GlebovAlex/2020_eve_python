class species:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print('assuming all species breathe')


class animals:
    def __init__(self,name,type):
        self.name = name,
        self.type = type

    def eat(self):
        print('eating abundantly')

    def sleep(self):
        print('sleeping deeply...')

class cat(animals):
    def meow(self):
        print('Meow meow')

class dog(animals,species):
    def jump(self):
        print('jumping joyously')

    def bark(self):
        print('bow bow')

class puppy(dog):
    def cute(self):
        print('just be cute')

x = puppy("pluto","pet")
x.eat()
x.breathe()
x.cute()