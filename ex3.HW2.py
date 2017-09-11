# Claudio Blanco Ex.2
# Excercise from the book
print("Hi there!")
print("I will now count my chickens:")
print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)
print("Now I will count the eggs:")
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)
print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)
print("Oh, that's why it's False.")

# Homework 2: Find the average of the following numbers
""" This section of code is my first attempt at the odd/even
number exercise"""

print(" i. Average for 44, 64, 88, 53, and 89 is: ", (44 + 64 + 88 + 53 + 89)/5)

print(" ii. Average for 39, 45 ,55, 90, and 96 is: ", (39 + 45 + 55 + 90 + 95 + 96)/6)

print(" iii. Average for 53, -45, -10, and 90 is:", (54 + (-45) + (-10) + 90)/4)

print(" iv. Average for 55, 65, 75, 95, and 32 is:", (55 + 65 + 75 + 95 + 32)/5)

print("Is the number 9 even?", 9 % 2 == 0)

print("Is the number 19 even?", 19 % 2 == 0)

print("Is the number 20 even?", 20 % 2 == 0)

# Here I try to lock the a number locked into a variable
answer = (3 % 2 == 0)
if answer == 0:
    print(f" {answer} is and odd number!")

answer = (19 % 2 == 0)
if answer == 0:
    print("9 is and odd number!")

# Here is my second attempt to the odd/even exercise
""" I was stuck here for a long time, but got some insight
after the class and returned to it. Much of the failure is not shown"""

print("Enter a number here: ")
num = input()
answer = (int(num) % 2)
# Mush of the failure was in the following piece of code
if answer == 1 : # The breakthrough came with changing the 0 to a 1
    print(f"{num} is an odd number!")
else: # For a while, having a 0 after the == sign made all answers print as even.
    print(f"{num} is an even number.")

# Claudio
