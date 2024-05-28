import math

class Shape:
    def __init__(self, type):
        self.type = type
        
    
class Rectangle(Shape):
    def __init__(self, type, width, height):
        super.__init__(self, type)
        width = self.width
        height = self.height
        
    def calc_area():
        area = width * height
        print(area)
        
    def calc_perimeter():
        perim = width * 2 + height * 2
        print(perim)

class Triangle(Shape):
    def __init__(self, type, base, length):
        super.__init__(self, type)
        
        base = self.base
        length = self.length
        
    def calc_area():
        area = 0.5 * base * length
        print(area)
        
    def calc_perimeter():
        

class Circle(Shape):
    def __init__(self, type, diameter):
        super.__init__(self, type)

        diameter = self.diameter
        
    def calc_area():
        area = math.pi * (self.diameter / 2) ** 2

print("Welcome to Shapes and Geometry!")

choice = input("1. Rectangle\n2. Triangle\n3. Circle")

if choice == "1":
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))
    rectangle1 = Rectangle(width, height)
    print(f"\nRectangle: Area = {rectangle1.calc_area()}\nPerimeter = {rectangle1.calc_perimeter()}")

if choice == 2:
    base = int(input("Enter the triangle base: "))
    length = int(input("Enter the triangle length: "))
    triangle1 = Triangle(base, length)
    print(f"\nTriangle: Area = {triangle1.calc_area()}\nPerimeter = {triangle1.calc_perimeter()}")
    
if choice == 3:
    
    


    