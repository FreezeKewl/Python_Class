#class Shapes():







class Shape(object):
    sides = None

    def __init__ (self, sides):
        self.sides = sides

    def perimeter(self):
        global
        perimeter = 0
        for side in self.sides:
            perimeter += sides
            return perimeter

    #def area(self):
triangle = Shape([3,4,5]) #create a variable triangle of type Shape
square = Shape([4,4,4,4])

print(triangle)
print("triangle sides:", triangle.sides)
print(triangle.perimeter())
print(square.sides)
print(square.perimeter())
