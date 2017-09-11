# Claudio Blanco Homework 3
"""
from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)
"""
"""
print(f"""
#Alright, so you said {likes} about liking me.
#You live in {lives}. Not sure where that is.
#And you have a {computer} computer. Nice.
""")
"""

from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("Please add words to the following the suggestions.")

print(f"Enter a verb ending in \"ing\".")
verb = input(prompt)

print(f"Enter a verb ending in \"ed\".")
verb2 = input(prompt)

print(f"Enter another verb ending in \"ed\".")
verb3 = input(prompt)

print(f"Enter a noun.")
noun = input(prompt)

print(f"Enter a verb.")
verb4 = input(prompt)

print(f"Enter a type of animal.")
animal = input(prompt)

print(f"Enter a noun.")
noun2 = input(prompt)

print(f"Enter another noun.")
noun3 = input(prompt)

print(f"Enter another noun.")
noun4 = input(prompt)

print(f"Enter the name of a place.")
place = input(prompt)

print(f"Enter a number.")
number = input(prompt)

print(f"""I was {verb} along mainstreet when a large-eyed green being {verb2}
me. I was {verb3} into their {noun} and it blasted off into the cosmos.
Then, the extraterrestrial asked me to {verb4} on the Tell-Lie-Vision.
I was suprised they spoke with an english slang. These unearthly beings had a
pet {animal}. We were hungry, so we ordered a {noun2} and it tasted like
chicken. As we came back into the Milky Way, one of the green, space beings
asked me if I wanted a {noun3}. I said No, but I would like a {noun4}.
He simply thought it into existence and then dropped me off in {place}.
Upon arrival, I realized I've been gone for {number} years and my identity was changed to {user_name}!
""")
