import time
"""
Write two Python functions to find the minimum number in a list. 
The first function should compare each number to every other number on the list. O(n2). 
The second function should be linear O(n)
"""


def findMin(a_list):

    overallMin = a_list[0]
    for i in a_list: # 1st loop
        is_smallest = True
        for j in a_list: # 2nd loop = O(n^2)
            if j > i:
                is_smallest = False 
        if is_smallest:
            overallMin == i

    return overallMin


some_list = [1,44,77,200,32]
print(findMin(some_list))

# Q: Why O(n^2)?
# A: count the nested loops
