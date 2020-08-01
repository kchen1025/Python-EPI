from typing import List

from test_framework import generic_test


def plus_one(arr: List[int]) -> List[int]:
    # TODO - you fill in here.
    arr.reverse()
    car = 1

    for i in range(len(arr)):
        if car == 0: break
        if car == 1:
            if arr[i] + car >= 10:
                arr[i] = 0
            else:
                arr[i] += car
                car = 0
    if car == 1:
        arr.append(1)
    arr.reverse()

    return arr  


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
