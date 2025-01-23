class Car:
    #What are the properties of this class?

    def __init__(self, make, model, year): #This is like a constructor. 
        self.make = make
        self.model = model
        self.year = year
        self.gas = 0

    def startEngine(self):
        print("Engine Started")
    
    def presentation(self):
        print(f"This is a {self.make} {self.model} from {self.year}")
    
    def pumpGas(self, amount):
        self.gas += amount
        print(f"Gas pumped: {amount} gallons")
        print(f"Current gas level: {self.gas} gallons")
    
    def drive(self, amount):
        if self.gas >= amount:
            self.gas -= amount
            print(f"You have been driving for {amount} miles")
        else:
            print("Not enough gas")


# car1 = Car()                    #This is calling the class
# print(car1.model)               #This is calling the model property of the class
# car1.startEngine()              #This is calling the startEngine method of the class

# car1 = Car("Toyota", "Corolla", 2020)
# car2 = Car("Honda", "Civic", 2019)  

# car1.presentation()
# car2.presentation()

mycar = Car("BMW", "i7", 2025)
print(mycar.gas)
mycar.pumpGas(100)
print(mycar.gas)    
mycar.drive(10)
mycar.drive(30)
print(mycar.gas)    


#This is adding cars to the current car inventory
#We have first a store with no inventory of cars whatsoever

car_inventory = []  

#This is function that will iterate every time we entered all the details of a car. 
for i in range(3):
    make = input("Enter make: ")    
    model = input("Enter model: ")  
    year = int(input("Enter year: "))   
    car_inventory.append(Car(make, model, year))    #It adds each car to the inventory.

#For every car in the list, we will print each car information. 
for car in car_inventory:
    car.presentation()               #We are calling the presentation method of the class which will print the car information.

    
     