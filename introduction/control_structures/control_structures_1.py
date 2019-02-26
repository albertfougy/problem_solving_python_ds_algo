import math
'''
While statement repeats body of code as long as a condition is true.
'''
# counter = 1
# while counter <=5:
#     print ("Hello World")
#     counter += 1

'''
While fragment where both conditions are satisfied
'''
# counter = 1
# done = False
# while counter <=10 and not done:
#     print("Hello World")
#     counter +=1

'''
for statement can be used to iterate over the members of a collection, 
so long as the collection is a sequence (list, tuples, and strings).
'''
# for item in [1,2,3,4,5,6,7]:
#     print(item)

'''
A common use of the for statement is to implement 
definite iteration over a range of values.
'''

# for item in range(5):
#     print(item **2)

'''
The following code fragment iterates over a list of strings and for each string 
processes each character by appending it to a list. The result is a list of all 
the letters in all of the words.
'''

# wordlist = ['cat','dog','rabbit']
# letterlist = [ ]
# for aword in wordlist:
#     for aletter in aword:
#         letterlist.append(aletter)
# print(letterlist)

'''
if and ifelse statement
'''
# num = input("Please enter value: ")
# n = int(num)
# if n<0:
#     print ("Sorry , value is negative")
# else:
#     print(math.sqrt(n))


'''
Selection constructs, as with any control construct, can be nested so that the 
result of one question helps decide whether to ask the next. 
'''

# num = input("Please enter your score: ")
# score = int(num)
# if score>=90:
#     print('A')
# else:
#     if score>=80:
#         print('B')
#     else:
#         if score>=70:
#             print('C')
#         else:
#             if score>60:
#                 print('D')
#             else:
#                 print('You have a BIG FAT "F"')

'''
Refactored with "elif"
'''


# num = input("Please enter your score: ")
# score = int(num)
# if score>=90:
#     print('A')
# elif score>=80:
#     print('B')
# elif score>=70:
#     print('C')
# elif score>60:
#     print('D')
# else:
#     print('You have a BIG FAT "F"')

'''
A single way selection construct, the if statement.
With this statement, if the condition is true, an action is performed. In the 
case where the condition is false, processing simply continues on to the next 
statement after the if
'''
# n=20
# if n<0:
#     n = abs(n)
# print(math.sqrt(n))
