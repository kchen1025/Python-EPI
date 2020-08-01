from typing import List

from test_framework import generic_test
import math

def next_permutation(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return []

    dip = None
    for i in reversed(range(1,len(arr))):
        if arr[i-1] < arr[i]:
            dip = i-1
            break;
    if dip == None: return []

    for i in reversed(range(dip+1, len(arr))):
        if arr[i] != arr[dip] and arr[i] > arr[dip]:
            arr[i],arr[dip] = arr[dip],arr[i]
            break;

    arr[dip+1:] = reversed(arr[dip+1:])
    return arr



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
