import random
import string
import itertools
import Levenshtein

ALLOWED_CHARS = string.ascii_lowercase + ''


# random.choice, which just chooses a random element from a sequence and _ as a
# placeholder for the unused loop variable.

# def generate(strlen):
#     alphabet = "abcdefghijklmnopqrstuvqxyz "
#     value = ""
#     for letter in range(strlen):
#         value += alphabet[random.randrange(27)]
#
#     return value



def generate(n):
    return ''.join(random.choice(ALLOWED_CHARS) for _ in range(n))

# def score(goal, teststring):
#     numSame = 0
#     for i in range(len(goal)):
#         if goal[i] == teststring[i]:
#             numSame = numSame + 1
#     return numSame / len(goal)

"""
refactored
"""

# def score(user_sentence, sentence):
#     return sum(user_char == char for user_char, char in zip(user_sentence, sentence))

"""
Alternatively, you could use the Levenshtein distance as score:
"""

def score(user_sentence, sentence):

    return len(user_sentence) - Levenshtein.distance(user_sentence, sentence)



# def main():
#     goal_string = "methinks it is like a weasel"
#     new_string = generate(28)
#     best_score = 0
#     best_string = ""  # modified
#     new_score = score(goal_string, new_string)
#     loop_count = 0  # modified
#     while new_score < 1:
#         if new_score > best_score:
#             print(new_score, new_string)
#             best_score = new_score
#
#             best_string = new_string  # modified
#         new_string = generate(28)
#         new_score = score(goal_string, new_string)
#
#         # last control statement added
#         if loop_count % 1000000 == 0:
#             print(best_score, best_string)
#         loop_count += 1
#


def main(user_sentence):
    n = len(user_sentence)
    max_score = 0
    best_fit = " " * n

    sentence = generate(n)
    for i in itertools.count():
        if sentence == user_sentence:
            # We are done
            print (i)
            break

        # Calculate score of current sentence and update best score if necessary
        current_score = score(user_sentence, sentence)
        if current_score > max_score:
            max_score = current_score
            best_fit = sentence

        # Output every 1000000 iterations
        if i % 1000000 == 0:
            print( i, best_fit, max_score)

        # Get a new random sentence
        sentence = generate(n)

if __name__ == "__main__":

    main("methinks it is like a weasel")
