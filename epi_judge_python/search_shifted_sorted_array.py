from typing import List

from test_framework import generic_test


def search_smallest(arr: List[int]) -> int:
    if not arr: return -1

    # sorted array
    if arr[0] <= arr[-1]:
        return 0

    low,high = 0,len(arr)-1
    pivot = arr[0]

    while low <= high:
        mid = (low+high)//2

        # found
        if arr[mid-1] > arr[mid]:
            return mid

        #right
        if pivot <= arr[mid]:
            low = mid+1
        else:
            #left
            high = mid-1
    return -1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
