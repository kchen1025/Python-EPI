import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, arr: List[str]) -> int:
    # loop until size and create a final count, if 'a' then add 1, 'b' remove 1
    finalSize = size
    for i in range(size):
        if arr[i] == 'a':
            finalSize += 1
        elif arr[i] == 'b':
            finalSize -= 1

    # now that we have final size, iterate backward and insert
    curs = finalSize
    for i in reversed(range(size)):
        print(curs,i)
        if arr[i] == 'a':
            arr[curs] = 'd'
            arr[curs-1] = 'd'
            curs -= 2
        elif arr[i] != 'b':
            arr[curs] = arr[i]
            curs-=1

    return finalSize



@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    print(replace_and_remove(24,
	["b", "d", "c", "a", "b", "a", "d", "b", "d", "b", "b", "a", "d", "c", "c", "a", "d", "a", "d", "d", "d", "b", "c", "c", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]))
    # arr = ['a','b','a','c','']
    # print(replace_and_remove(4,arr))
    # print(arr)

    # exit(
    #     generic_test.generic_test_main('replace_and_remove.py',
    #                                    'replace_and_remove.tsv',
    #                                    replace_and_remove_wrapper))
