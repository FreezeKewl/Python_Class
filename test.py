import math

class MyClass():
    """A simple example class"""
    def __init__(self, one, two):
        self.i = one
        self.f = two

    i = 12345
    pi = 3.142
    def f(self):
        return 'hello world'



print(MyClass.i)
print(MyClass.f)
#print(MyClass.__dict__)
#print(MyClass.f.__dict__)
x = MyClass(123, 567)

print(x.i)
print(x.f)

x = MyClass(321, 765)

print(x.i)
print(x.f)
print(MyClass(135, 246))


class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius

r=int(input("Enter radius of circle: "))
obj=circle(r)
print("Area of circle:",round(obj.area(),2))
print("Perimeter of circle:",round(obj.perimeter(),2))

"""
class Shapes():
    def perimeter():

    def area():
"""
