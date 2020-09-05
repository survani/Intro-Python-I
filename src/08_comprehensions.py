"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [numbers for numbers in range(1, 6)]

print("Produce Array 1-5:", y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# This works by doing the power of 3 to each value inside the array "object".
"""
This works like this: ( Everything inside the ( ) is the index. )
array [ (0)**3 = 0 , (1)**3 = 1, (2)**3 = 8 ... ] 
"""
y = [numbers**3 for numbers in range(10)]

print("Cubes of the Numbers:", y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [text.upper() for text in a]

print("Uppercase Array:", y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [even for even in x if int(even) % 2 == 0]

print(y)
