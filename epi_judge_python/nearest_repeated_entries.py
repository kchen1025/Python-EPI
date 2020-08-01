from typing import List

from test_framework import generic_test

import math

def find_nearest_repetition(paragraph: List[str]) -> int:
    d = {}
    closestDist = math.inf

    for i,word in enumerate(paragraph):
        if word in d:
            closestDist = min(closestDist, i-d[word])
        d[word] = i
    return closestDist if closestDist != math.inf else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
