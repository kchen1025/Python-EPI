import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', '', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(string):
    p1,p2 = 0,0

    while p1 < len(string) and p2 < len(string):
        while p1 < len(string) and not string[p1].isalnum():
            p1+=1

        p2 = p1

        while p2 < len(string) and string[p2].isalnum():
            p2+=1

        string[p1:p2] = reversed(string[p1:p2])
        p1 = p2

    if p2 >= len(string):
        string[p1:p2] = reversed(string[p1:p2])

    return string.reverse()

@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    # yeet = ['r', 'a', 'm', '', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y']
    # reverse_words(yeet)
    # print(yeet)
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
