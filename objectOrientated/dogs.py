# Object orientated Programming in python


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def add_one(self, x):
        return x + 1

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age
