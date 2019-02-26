"""
In the time module there is a function called time that will return the current
system clock time in seconds since some arbitrary starting point. By calling this
function twice, at the beginning and at the end, and then computing the difference,
we can get an exact number of seconds (fractions in most cases) for execution.
"""
import time

# Listing 1
def sumOfN2(n):
    start = time.time()

    theSum = 0
    for i in range(1, n+1):
        theSum +=i

    end = time.time()

    return theSum, end-start

# invoke function 5 times
for i in range(5):
    # computing sum with first 10,000 integers
    print("Sum is %d required %10.7f seconds"%sumOfN2(10000))

for i in range(5):
    # computing sum with first 100,000 integers
    print("Sum is %d required %10.7f seconds"%sumOfN2(100000))

for i in range(5):
    # computing sum with first 1,00,000 integers
    print("Sum is %d required %10.7f seconds"%sumOfN2(1000000))

