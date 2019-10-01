class Dog:
    def __init__(self, type, name, age, param):
        self.type = type
        self.name = name
        self.age = age
        self.param = param

    def produce_sound(self,):
        print("I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.")

class Cat:
    def __init__(self,type,name, age, param):
        self.type = type
        self.name = name
        self.age = age
        self.param = param

    def produce_sound(self,):
        print("I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.")

class Snake:

    def __init__(self,type, name, age, param):
        self.type = type
        self.name = name
        self.age = age
        self.param = param

    def produce_sound(self,):
        print("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")


animals = []

data = input()

while data != "I'm your Huckleberry":

    animal = None
    try:
        type, name, age, param = list(data.split())
        if type == "Dog":
            animal = Dog(type, name, age, param)
        elif type == "Cat":
            animal = Cat(type, name, age, param)
        elif type == "Snake":
            animal = Snake(type, name, age, param)
        animals.append(animal)

    except:
        for a in animals:
            if a.name == list(data.split())[1]:
                a.produce_sound()
                continue

    data = input()

for anim in animals:

    if anim.type == "Dog":
        print(f"Dog: {anim.name}, Age: {anim.age}, Number Of Legs: {anim.param}")
    elif anim.type == "Cat":
        print(f"Cat: {anim.name}, Age: {anim.age}, IQ: {anim.param}")
    elif anim.type == "Snake":
        print(f"Snake: {anim.name}, Age: {anim.age}, Cruelty: {anim.param}")

