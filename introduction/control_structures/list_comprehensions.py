'''
create a list of the first 10 perfect squares, we could use a for statement:
'''

# sqlist = []
# for x in range(1, 11):
#     sqlist.append(x*x)
# print(sqlist)

'''
rewritten as list comprehension
'''

# def list_comp():
#     sqlist = [x**2 for x in range(1,11)]
#     return sqlist

# print(list_comp())

'''
filter out result for odds
'''

# def list_comp():
#     sqlist = [x*x for x in range(1,11) if x%2 != 0]
#     return sqlist

# print(list_comp())

'''
filter out vowels and make them upper case if they don't already exist
'''

def list_comp_upcase(characters):
    # "not in" can be rewritten (in your mind) "IF IT'S NOT ALREADY THERE"
    upcase = [char.upper() for char in characters if char not in 'aeiou']
    return upcase

print(list_comp_upcase('comprehension'))

'''
experimenting with nested list comprehension with unpacking args
'''

# def list_comp_upcase(*args):
#     upcase = [chr.upper() for char in args for chr in char if chr not in 'aeiou']
#     return upcase

# comp = ['comprehension', 'list']
# print(list_comp_upcase(*comp))