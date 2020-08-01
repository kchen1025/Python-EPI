from test_framework import generic_test


def square_root(x: float) -> float:
    low,high = 0,x

    while low <= high:
        mid = (low+high)/2

        if mid == x:
            return mid

        if mid < x:

        else:

    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
