from typing import Iterator

from test_framework import generic_test

import collections

def majority_search(stream: Iterator[str]) -> str:
    # set letter to the first in stream
    candidate = next(stream)
    count = 1

    for val in stream:
        # if val is same as candidate, add to count
        if val == candidate:
            count += 1
        else:
            count -=1
        if count == 0:
            candidate = next(stream)
            count = 1

    return candidate







































    # # loop through stream, keep a candidate with a count of 1
    # # if new char is not the same as candidate, decrement count
    # # if count = 0, we must set the new cand to i+1
    # cand = next(stream)
    # count = 1
    #
    # for char in stream:
    #     if char == cand:
    #         count += 1
    #     else:
    #         count -= 1
    #
    #     if count == 0:
    #         cand = next(stream)
    #         count = 1
    # return cand


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    # print(majority_search(iter(['b','a','c','a','a','b','a','a','c','a'])))
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
