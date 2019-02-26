'''
The algorithm uses the idea of an accumulator variable that is initialized to 0.
The solution then iterates through the n integers, adding each to the accumulator.
'''

def sumOfN(n):
    theSum = 0
    for i in range(1, n+1):
        theSum += i

    return theSum

print(sumOfN(10))