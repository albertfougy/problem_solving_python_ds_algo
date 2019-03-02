"""
OBJECTIVE:
generate a random 28 char string, compare it to the target string,
score the generated string based on similarity to target, repeat the
process until there is a 100% match
https://runestone.academy/runestone/static/pythonds/Introduction/DefiningFunctions.html
"""

import random


def attempt(strlen):
    alphabet = "abcdefghijklmnopqrstuvqxyz "
    value = ""
    for letter in range(strlen):
        value += alphabet[random.randrange(27)]

    return value


def score(goal, teststring):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numSame = numSame + 1
    return numSame / len(goal)


def main():
    goal_string = "methinks it is like a weasel"
    new_string = attempt(28)
    best_score = 0
    best_string = ""
    new_score = score(goal_string, new_string)
    loop_count = 0
    while new_score < 1:
        if new_score > best_score:
            print(new_score, new_string)
            best_score = new_score
            best_string = new_string
        new_string = attempt(28)
        new_score = score(goal_string, new_string)

        if loop_count % 1000000 == 0:
            print(best_score, best_string)
        loop_count += 1


if __name__ == "__main__":

    main()
