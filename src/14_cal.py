"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

# resouces used to complete this

# sys.argv: https://stackoverflow.com/questions/4117530/sys-argv1-meaning-in-script
# also https://www.pythonforbeginners.com/system/python-sys-argv

# int(): https://www.programiz.com/python-programming/methods/built-in/int

# == or is usage below:
# https://www.geeksforgeeks.org/difference-operator-python/#:~:text=The%20%3D%3D%20operator%20compares%20the,the%20same%20object%20or%20not.&text=We%20can%20check%20it%20with,%E2%80%9Cidentity%E2%80%9D%20of%20an%20object.


import sys
import calendar
from datetime import datetime

# 1st Step
amnt_args = len(sys.argv)

# 2nd Step - No input specified
if amnt_args == 1:
    mm = datetime.now().month
    yy = datetime.now().year

# 3rd Step - User inputs 1 argument
    # we are assuming that the user input was for the month, but the year will continue to output datetime.now().year.
elif amnt_args == 2:
    # The sys.argv[1] looks into the first argument.
    # "The int() method returns an integer object from any number or string." - programiz.com
    mm = int(sys.argv[1])
    yy = datetime.now().year

# 4th Step - User inputs 2 arguments
elif amnt_args == 3:
    # The sys.argv[1] looks into the first argument.
    # The sys.argv[2] looks into the second argument.
    mm = int(sys.argv[1])
    yy = int(sys.argv[2])


else:
    print("How to use: [Month] [Year]")

    # "sys.exit() is considered good to be used in production code for the sys module is always available."
    # geeksforgeeks.org
    sys.exit(0)

new_calendar = calendar.TextCalendar()
new_calendar.prmonth(yy, mm)
