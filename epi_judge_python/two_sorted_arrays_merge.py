from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    insertIdx = m+n-1
    c1,c2 = m-1, n-1

    while c1 >= 0 and c2 >= 0:
        if A[c1] > B[c2]:
            A[insertIdx] = A[c1]
            c1-=1
        else:
            A[insertIdx] = B[c2]
            c2-=1
        insertIdx-=1
    while c2 >=0:
        A[insertIdx] = B[c2]
        c2-=1
        insertIdx-=1



def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
