from typing import List

from test_framework import generic_test


def search_first_of_k(arr: List[int], target: int) -> int:
    low,high = 0,len(arr)-1

    while low <= high:
        mid = (low+high)//2

        if target <= arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return low if low >= 0 and low < len(arr) and arr[low] == target else -1


    6th


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
