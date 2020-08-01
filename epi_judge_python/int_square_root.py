from test_framework import generic_test


def square_root(k: int) -> int:
    if k == 1: return 1

    low,high = 0,k//2

    closest = None

    while low <= high:
        mid = (low+high)//2

        if k >= mid**2:
            low = mid+1
            closest = mid
        else:
            high = mid - 1

    return closest

    

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
