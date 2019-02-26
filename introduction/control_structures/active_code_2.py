# modify code to produce this result so that the final list only 
# contains a single copy of each letter.
# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']

wordlist = ['cat','dog','rabbit']
letter_list = []
for a_word in wordlist:
    for a_letter in a_word:
        if a_letter not in letter_list:
            letter_list.append(a_letter)
print(letter_list)