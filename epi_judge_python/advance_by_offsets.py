from typing import List

from test_framework import generic_test




def can_reach_end(arr):
    max_reach = 0
    i = 0

    while i <= max_reach:
        max_reach = max(max_reach, i+arr[i])
        if max_reach >= len(arr)-1: return True
        i+=1
    return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
