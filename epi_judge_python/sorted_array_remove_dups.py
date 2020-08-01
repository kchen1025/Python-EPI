import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(arr: List[int]) -> int:
    if len(arr) <= 1: return len(arr)

    write = 1
    for i in range(1,len(arr)):
        if arr[write-1] != arr[i]:
            arr[write] = arr[i]
            write+=1

    return write



@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    # print(delete_duplicates([-8, -7, -6, -5, -5, -4, -3, -1, -1, 0, 0, 2, 2, 2, 4]))
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
