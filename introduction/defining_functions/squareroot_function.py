
import math

"""
Newton’s Method for approximating square roots performs an iterative computation
that converges on the correct value. 
"""



# def squareroot(n):
#     root = n/2    #initial guess will be 1/2 of n
#     for k in range(20):
#         root = (1/2)*(root + (n / root))
#
#     return root


"""
Remix using what I have learned so far. Implementing modularity via helper 
function. Helper function to raise exceptions on negative numbers.
"""


def squareroot(n):
    helper_except(n)
    root = n / 2
    for k in range(20):
        root = (1 / 2) * (root + (n / root))
    return root

def helper_except(the_error):
    if the_error < 0:
        raise RuntimeError ("You can't use a negative number")


def main():
    input_user = int(input("Enter number for square root: "))
    print(squareroot(input_user))


if __name__ == "__main__":
    main()
