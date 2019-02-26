import time
"""
This function, sumOfN3, takes advantage of a closed equation ∑ni=1 i=(n)(n+1)/2 
to compute the sum of the first n integers without iterating.
"""

# summation without iteration

def sumOfN3(n):
    start = time.time()
    sumTotal = (n*(n+1))/2   
    end = time.time()
    return sumTotal, end - start

print("Sum is %d required %10.7f seconds"%sumOfN3(10000))
print("Sum is %d required %10.7f seconds"%sumOfN3(100000))
print("Sum is %d required %10.7f seconds"%sumOfN3(1000000))
print("Sum is %d required %10.7f seconds"%sumOfN3(10000000))
print("Sum is %d required %10.7f seconds"%sumOfN3(100000000))