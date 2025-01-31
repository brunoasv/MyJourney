import math
"""
Create a class Circle that has a method for the radius, diameter, perimeter, and area of the circle.
It should also contain 2 functions: calculate_area and calculate_perimeter.
Also, another function to print its values.
"""

class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius**2
        self.perimeter = 0
        self.area = 0

    def print_values(self):
        print(f"Radius: {self.radius}")
        print(f"Diameter: {self.diameter}")
        print(f"Perimeter: {self.perimeter}")
        print(f"Area: {self.area}")


    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        self.perimeter = perimeter
    
    def calculate_area(self):
        area = math.pi * self.diameter
        self.area = area
    
       
     
    
circle1 = Circle(3.5)   
circle1.print_values()
circle1.calculate_area()
circle1.calculate_perimeter()
circle1.print_values()  
   