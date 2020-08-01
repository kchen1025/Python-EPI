from test_framework import generic_test

import collections
def is_letter_constructible_from_magazine(letter_text: str, magazine_text: str) -> bool:
    # count magazinte text characters first
    chars = collections.defaultdict(int)
    for char in magazine_text:
        chars[char] += 1

    # loop through letter_texts, and subtract from the magazine test dictionary.
    # if at any point we fall below 0 for any chracter, return false
    # if we make it , return true
    for char in letter_text:
        if char not in chars:
            return False
        elif chars[char] == 0:
            return False
        else:
            chars[char] -= 1
    return True 



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
