# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(x):
    # when x / 2 has a remainder of 0 then x is even.
    if x % 2 == 0:
        return True
    else:
        return False


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)


# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def checking_number(x):
    if is_even(x):
        print("Even!")
    elif not is_even(x):
        print("Odd")


checking_number(num)

# done
