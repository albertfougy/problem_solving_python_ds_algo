__author__ = 'albertfougy'
import time
from random import randrange

"""
Test function with random string size and time alloted to perform comparisons
"""

# exponential version == O(n**2)

# def findMin(a_list):
#     overallMin = a_list[0]
#     for i in a_list: # 1st loop
#         is_smallest = True
#         for j in a_list: # 2nd loop = O(n^2)
#             if j > i:
#                 is_smallest = False 
#         if is_smallest:
#             overallMin == i
#     return overallMin


# linear version == O(n)

def findMin(a_list):
    minsofar= a_list[0]
    for i in a_list:
        if i < minsofar:
            minsofar == i
    return minsofar



some_list = [1,44,77,200,32]
print(findMin(some_list))

for listSize in range(1000, 10001,1000):
    a_list = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMin(a_list))
    end = time.time()
    # print("size: %d time: %f" % (listSize, end-start))
    print(f'size: {listSize} time: {end-start}')
