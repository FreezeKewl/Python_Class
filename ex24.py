# The next 3 lines are print statements
print("Let's practice everything.") # This print statement is a regular print statement
print('You\'d need to know \'bout escapes with \\ that do:') # This print statement inclued escapes
print('\n newlines and \t tabs.') # This print statement includes a newlines and tabs

# The following is the variable "poem" which has a poem assigned to it
# The = sign indicates assignment and the """ symbols create a multi-line content for the variable
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requiresss an explanation
\n\t\twhere there is none.
"""

print("------------")
print(poem) # prints the poem assigned to the variable "poem" above
print("------------")

five = 10 - 2 + 3 - 6 # "five" is a variable that has the result of mathimatical computation assigned to it
print(f"This should be five: {five}") # This line is a print statement that includes the variable "five" from above

# the following line is a function named "secret_formula" with the word "started" as a parameter
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000 # start_point is a variable  with the number 1000 assigned to it
# beans, jars, & crates are a sequence of variables assigned the formula secret_formula(start_point)
beans, bars, boxes = secret_formula(start_point) # """*Here, I changed all the variables inside the function

# remember that this is another way to format a string (FROM THE BOOK)
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string (FROM THE BOOK)
print(f"We'd have {beans} beans, {bars} jars, and {boxes} crates.") # *I changed the variables here to match the changes in line 33

start_point = start_point /10 # he start_point variable is reassigned a value by dividing the original value by 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string (FROM THE BOOK)
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
