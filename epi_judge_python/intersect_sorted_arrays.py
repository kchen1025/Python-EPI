from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(a: List[int], b: List[int]) -> List[int]:
    c1, c2 = 0,0
    output = []

    while c1 < len(a) and c2 < len(b):
        if a[c1] < b[c2]:
            c1+=1
        elif a[c1] > b[c2]:
            c2+=1
        else:
            output.append(a[c1])
            while c1 < len(a) and a[c1] == b[c2]:
                c1+=1
    return output


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
