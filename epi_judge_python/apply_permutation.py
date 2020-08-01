from typing import List

from test_framework import generic_test


def apply_permutation(p: List[int], arr: List[int]) -> None:
    for i in range(len(p)):
        while p[i] != i:

            arr[i],arr[p[i]] = arr[p[i]],arr[i]
            p[p[i]],p[i] = p[i],p[p[i]]            

    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    # print(apply_permutation([2,0,1,3],['a','b','c','d']))
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
