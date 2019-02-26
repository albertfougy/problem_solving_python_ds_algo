wordlist = ['cat', 'dog', 'rbi']
letterlist = []
for a_word in wordlist:
    for a_letter in a_word:
        letterlist.append(a_letter)
print(letterlist)

# ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']