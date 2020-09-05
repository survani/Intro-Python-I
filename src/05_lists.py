# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
x.append(4)
print("Appended 4 into list of x: ", x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)
print("Extended y to the list of x: ", x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)
print("Removed 8 from list x: ", x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print("Inserted 99 into the list x: ", x)

# Print the length of list x
# YOUR CODE HERE
print("Final length of list x: ", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE

for numbers in x:
    print("list x values * 1000: ", numbers * 1000)
