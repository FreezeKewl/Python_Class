# First half of homework #5
import math

# 1. This print statement prints out the question to be answered by the Min2Sec() function

print("How many seconds are there in 42 minutes and 42 seconds?")
# Next line is the Min2Sec() function
def Min2Sec():
    Sec = ((42 * 60) + 42)# this variable holds the value of the conversion
    # Pint statement prints the value in a sentence form
    print(f"-There are {Sec} seconds in 42 minutes and 42 seconds.")
    #Line 10 calls the Min2Sec() function to run
Min2Sec()

# 2. This print statement prints out the question
print("How many miles are there in 10 kilometers?")
# The function contains the calculation to answer the question
def KM2Miles():
    KM = (10 * .621371)# Variable that contains the value/result of calculaion
    print(f"-There are {KM} miles in 10 Kilometers.")# Prints
# Line 19 calls the KM2Miles() function to run
KM2Miles()

# 3. Convert Fahrenheit to Celsius
print("How much is 83 degrees Fahrenheit in degrees Celsius?")

def Fah2Cel():
    Cel = round(((82 - 32) * 5/9), 2)

    print(f"83 degrees Fahrenheit is equal to {Cel} Celsius.")

Fah2Cel()

print("What is the square root of 81, 19, 16 and 12")

# 4.
lst = []
num = (81, 19, 16, 12)
for n in (num):
    lst.append(math.sqrt(n))
print("The Square Root of elements in given list is :", (lst))

# 5. Area of a circle with a radius 9
print("What is the area of a circle with a radius of 9")

area = math.pow(9, 2) * 3.14

print(f"The area of a circle with radius of 9 is {area}")

# 6. Finding x in a sentence in user inputted sentence

sentence = input("Type a random sentence of your choosing. Type here: ")
print(sentence)

if(sentence.count("x")):
    print("The sentence you typed has an x in it!")
else:
    print("Your sentence doesn't have the letter x.")

# 7.
def vowels():
    ranSent = input("Type a random sentence of your choosing. Type here:")
    print(sentence)

    if(ranSent.count("a, e, i, o, u")):
        print("The sentence you typed has a vowel in it!")
    else:
        print("Your sentnece doesn't have any vowels in it.")

vowels()

# Triangle exercise
print("\nEnter three numbers with spaces between them for \neach side of a triangle to determine \nis it's a triangle: ")
#numEntered.split(" ")
a, b, c = input().split(" ")
#print(a, b, c)

def triangle(a, b, c):

    if(a + b > c) and (a + c > b) and (b + c > a):
        print("This is a triangle")
    else:
        print("This is not a triangle")

triangle(a, b, c)
