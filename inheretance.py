class Animal:
    def __init__(self, weight, height, name):
        self.weight = weight
        self.height = height
        self.name = name

    def print_data(self):
        print(f"Name: {self.name}")
        print(f"Weight: {self.weight}")
        print(f"Height: {self.height}")

class mammal(Animal):                                    # Inheriting the Animal class
    def __init__(self, weight, height, name, gender):
        super().__init__(weight, height, name)           # Inheriting the properties of the parent class
        self.gender = gender                             # Adding new property to the child class
    
    def print_data(self):
        super().print_data()                             # Calling the parent class method
        print(f"Gender: {self.gender}")

    def reproduce(self):
        print(f"{self.name} is reproducing")

class Dog(mammal):
    def __init__(self, weight, height, name, gender, breed, owner):
        super().__init__(weight, height, name, gender)
        self.breed = breed
        self.owner = owner
    
    def print_data(self):
        super().print_data()
        print(f"Breed: {self.breed}")
        print(f"Owner: {self.owner}")

    def bark(self):
        print(f"{self.name} is barking")

animal1 = Animal(100, 5, "Lion")
animal1.print_data()
print("\n")
mammal1 = mammal(200, 6, "Tiger", "Male")
mammal1.print_data()
mammal1.reproduce()
print("\n")
dog1 = Dog(50, 2, "Tom", "Male", "Pug", "John")
dog1.print_data()
dog1.bark()
dog1.reproduce()

