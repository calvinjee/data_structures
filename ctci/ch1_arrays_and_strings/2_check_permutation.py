#1.2
# Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other

from collections import Counter


def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    str1_chars = {}
    str2_chars = {}

    for i in range(len(str1)):
        char1 = str1[i]
        if char1 in str1_chars:
            str1_chars[char1] += 1
        else:
            str1_chars[char1] = 1

        char2 = str2[i]
        if char2 in str2_chars:
            str2_chars[char2] += 1
        else:
            str2_chars[char2] = 1

    if str1_chars == str2_chars:
        return True

    return False


def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    counter = Counter()

    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1

    return True


if __name__ == "__main__":
    print(check_permutation('calvin', 'vinlac'))
    print(check_permutation('abc','def'))

