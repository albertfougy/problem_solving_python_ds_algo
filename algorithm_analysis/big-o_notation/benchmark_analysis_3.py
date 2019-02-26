"""
The number of assignment operations is the sum of four terms.
"""

 # Listing 2

# The FIRST TERM is the constant 3, representing the 
# three assignment statements at the start of the fragment
 a=5
 b=6
 c=10
# The SECOND TERM is 3n**2, since there are three statements 
# that are performed n**2 times due to the nested iteration. 
 for i in range(n):
     for j in range(n):
         x = i * j
         y = j * j
         z = i * j
# The THIRD TERM is 2n, two statements iterated n times.
for k in range(n):
    w = a*k + 5
    v = b*b
# Finally, the fourth term is the constant 1, 
# representing the final assignment statement. 
d=33


# This gives us T(n)=3+3n**2+2n+1=3n**2+2n+4. By looking at the exponents, we can 
# easily see that the n2 term will be dominant and therefore this fragment of 
# code is O(n**2). Note that all of the other terms as well as the coefficient 
# on the dominant term can be ignored as n grows larger.