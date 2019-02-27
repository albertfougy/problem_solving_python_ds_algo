__author__ = "albertfougy"

import math

"""
The code fragment below shows the result of creating a new RuntimeError exception. 
Note that the program would still terminate but now the exception that caused the 
termination is something explicitly created by the programmer.
"""

a_number = int(input("Please enter an integer: "))

if a_number < 0:
    raise RuntimeError("You can't use a negative number")
else:
    print(math.sqrt(a_number))


#   File "raise_exception.py", line 14, in <module>
#     raise RuntimeError("You can't use a negative number")
# RuntimeError: You can't use a negative number

