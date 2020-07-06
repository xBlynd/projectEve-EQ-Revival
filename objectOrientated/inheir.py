

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old')
    def speak(self):
        print("i don't know what i say")

# library for cats for some reason.....
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def speak(self):
        print('Meow')

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

# Dogs.... the real animal
class Dog(Pet):
    def speak(self):
        print('Bark')

p = Pet('Sterling', 6)
p.speak()

c = Cat('Lana', 1, 'Brown')
c.show()

d = Dog('Dinky', 25)
d.speak()
