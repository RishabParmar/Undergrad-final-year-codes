# Example of inheritance and method overriding


class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printStuff(self):
        print(self.name)
        print(self.age)


class Child(Parent):

    def __init__(self, name, age, ids):
        super().__init__(name, age)
        self.id = ids

    def printStuff(self):
        print(self.name)
        print(self.age)
        print(self.id)


objectt = Parent("Bob", 30)
objectt.printStuff()
child = Child("Joe", 20, 21)
child.printStuff()
