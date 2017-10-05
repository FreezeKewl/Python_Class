
import math

class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
obj=rectangle(a,b)
print("Area of rectangle:",obj.area())

print()

"""
perimeter
area
property: sides
4 instances of class
print out each attribute of the instance and use each method in the class
"""

class Shape():
    """
    def circle(pi,radius):
        area_circle = pi * (radius ** 2)
        print " the area of your circle equals %s" % (area_circle)
    def rectangle(length, width):
        area = length * width
        print "The area of your rectangle equals %s" %(area)
    def triangle(height, base):
        area_triangle = height * base * 0.5
        print "the area of your triangle equals %s" % (area_triangle)
    def square(length):
        area_square = length ** 2
        print "the area of your square equals %s" % (area_square)
    """
    # Circle pi * radius squared
    shapeType = input("Enter the shape you want the area for: a for circle, b for square, c for triangle ord for oval?: ")
    a = "circle"
    b = "square"
    c = "triangle"
    d = "oval"
    if shareType = a:
        r = int(input("What is the radius of your circle? "))

        pi = 3.142
        a = (2 * pi * r)
        print(f"The perimeter of your circle is {circle}.")
    elif shareType = b:
        l = int(input("What is the length of one side of your square? "))
        per_of_Sq = l * 4
        print(f"The perimeter of your square is {per_of_Sq}.")
    elif shareType = c:
        sides = ("Enter the three sides of your triangle: ")
        triangle = (side + side + side)
        print(f"Your triangle has the perimeter of {triangle}.")
    elif shareType = d:

#    else:
        print("Invalid input!")

"""
    def __init__(self, P, A):
        self.perimeter = P
        self.area = A



    def __init__(self, r, (r * 2)):
        self.Radius = r
        self.Circumference = r * 2


    Shape.__init__(self, l, w):
        self.length = l
        self.width = w

    Shape.__init__(self, maR, miR):
        self.majorRadius = maR
        self.minorRadius = miR

    def perimeter():
        pi = 3.142
        if(shapeType == circle):
            circle = ((2 * pi) * r)

        elif(shapeType == square):

        elif(shapeType == triangle):



        elif(shapeType == oval):
            maj = input("Please provide the major radius: ")
            minor = input("Please provide the minor radius now: ")
            area_of_oval = (maj * minor * pi)
            print(f" Area of oval or ellipse is equal to {area_of_oval} unit squared.")


    rectangle =






    def area():
"""
