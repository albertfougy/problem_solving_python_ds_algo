'''
re-do last challenge in list comprehension
For an extra challenge, see if you can figure out how to remove the duplicates.
'''

def list_comp_rmx(*word_list):
    print([a_letter for a_word in word_list for a_letter in a_word])

word_list = ['cat','dog','rabbit']
list_comp_rmx(*word_list)

# >> ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a', 'b', 'b', 'i', 't']

'''
remix with removing duplicate letters and retaining the original order
'''

# def list_comp_rmx(*word_list):
#     seen = set()
#     print([a_letter for a_word in word_list for a_letter in a_word 
#           if not (a_letter in seen or seen.add(a_letter))])



# word_list = ['cat','dog','rabbit']
# list_comp_rmx(*word_list)

# >> ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
