from __future__ import division
import datetime
import math
import time

# The volume of the sphere is : V = 4/3 × π × r3 = π × d3/6.
# Thevolume of a sphere with radius r is (4/3)pir3
print("What is the volume of a sphere with radius of 5?")

def volume_of_sphere():
    #pi = float(3.14)
    #radius = 5
    volume = (4/3) * (3.14 * math.pow(5, 3))
    print(volume)

volume_of_sphere()


""" 10)  Write a boolean function that returns true if
a given input is divisible by 3 or return false otherwise
"""

#print(input("Please enter a random number here: "))

def cubes():
    number = int(input("Please enter a random number here: "))
    num = (number % 3)
    if int(num == 0):
        print(f"The number {number} is divisible by 3")

    else:
        print(f"The number {number} is not divisible by 3")

cubes()

# 11)  Import date/time  library and print out today's date and time

today = datetime.datetime.today()
print ("\nThe current date and time:")
print(today.strftime(" %Y-%m-%d %H:%M"))
#print(today)

# 12) Using the date/time library, print out the current year

today = datetime.datetime.today()
print ("\nThe current year is:")
print(today.strftime(" %Y"))

# 13) write a function that counts how many times the letter a is repeated in a given word (get the work from the user as an input)

def letterA():
    letter = str(input("Please type out a sentence here: "))
    a = ["a"]
    acount = [0]
    for i in range(len(letter)):
        for v in range(len("a")):

            if letter[i] == a[v]:
                acount[v] += 1

    for i in range(len(a)):
        print(letter[i], ":", acount[i])

letterA()

# 14) Write code that counts the number of letters in a word provided by the user_name

def letters_in_a_word():
    word = str(input("Please type in a word to find how many letters it contains: "))
    letters = len(word)
    print(letters)
    print("\n")


letters_in_a_word()

# 15) Write a function that counts down from 20.

def countdown(t):
    while t > 0:
        print(t)
        t = t - 1
        if t == 0:
            print("0,the End!")

countdown(20) # not an actual second by second countdown

# 16) Write a function that tells if the given input is even or odd

def odd_even():
    num = int(input("\n Type in any number here: "))
    #print(num)
    if (num % 2 == 0):
        print("Your number is even!")
    else:
        print("Your number is odd!")
odd_even()
print("\n")

# 17) find the length of a string given by the user as input using a counter variiable (don't use the built-in len function)

length=0
for x in "This is a string":
    length += 1
print(length)

def find_length():
    count = 0
    sentence = input("\n Please enter a sentence here: ")
    for i in sentence:
        count = count + 1
        print(f"The length of the sentence is: {count}")
        
    #return sum(1 for char in sentence)

find_length()
# 18) Write a loop  that traverse through a string provided by the user and prints out one letter at a time

def find_length2():
    sentence = input("\n Please enter a sentence here: ")
    for i in sentence:
        print(i[0])

find_length2()
