# 1.1
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


def is_unique(str):
    seen = {}
    for char in str:
        if char not in seen:
            seen[char] = True
        else:
            return False

    return True


def is_unique2(str):
    for i in range(len(str) - 1):
        for j in range(i + 1, len(str)):
            if str[i] == str[j]:
                return False

    return True


def is_unique3(str):
    if len(str) > 128:
        return False

    chars = [False for _ in range(128)]

    for char in str:
        value = ord(char)
        if chars[value]:
            return False

        chars[value] = True

    return True


if __name__ == "__main__":
    print(is_unique('calvin'))
    print(is_unique('hahaha'))

    print(is_unique2('calvin'))
    print(is_unique2('hahhh'))

    print(is_unique3('calvin'))
    print(is_unique3('hahhh'))

