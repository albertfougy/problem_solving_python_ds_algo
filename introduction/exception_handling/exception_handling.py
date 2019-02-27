__author__ = "albertfougy"

import math

anumber = int(input("Please enter an integer: "))
# print(math.sqrt(anumber))


# >> Please enter an integer: -23
# Traceback (most recent call last):
#   File "exception_handling.py", line 4, in <module>
#     print(math.sqrt(anumber))
# ValueError: math domain error




"""
We can handle this exception by calling the print function from within a try block. 
A corresponding except block “catches” the exception and prints a message 
back to the user in the event that an exception occurs.
"""

try:
    print(math.sqrt(anumber))
except ValueError:
    print("Bad value for square root")
    print("Using abs value instead")
    print(math.sqrt(abs(anumber)))



# >> Please enter an integer: -23
# Bad value for square root
# Using abs value instead
# 4.795831523312719
