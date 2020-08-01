from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:

    def helper(row):
        if row == n:
            result.append(col_placement.copy())
            return True

        for col in range(n):
            # if all(abs(c - col) not in (0, row - i) for i,c in enumerate(col_placement[:row])):
            if not isBlocked(col_placement, row, col):
                col_placement[row] = col
                helper(row+1)

    result = []
    col_placement = [0] * n
    helper(0)
    return result

def isBlocked(col_placement, row, col):
    for i,c in enumerate(col_placement[:row]):
        if col == c or abs(col - c) == (row - i):
            return True
    return False

def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))









































    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # def solve_n_queens(row):
    #     if row == n:
    #         result.append(col_placement.copy())
    #         return
    #
    #     for col in range(n):
    #         # the 0 refers to a placment being in the same col, the others refer to rows 1 away need to be at 1 diag, rows 2 away need to be at 2 diag etc
    #         if(all( abs(c - col) not in (0, row - i)  for i,c in enumerate(col_placement[:row]))):
    #             col_placement[row] = col
    #             solve_n_queens(row+1)
    #
    #
    #
    # result = []
    # col_placement = [0]*n
    # solve_n_queens(0)
    # return result










#if all(abs(c - col) not in (0, row - i) for i,c in enumerate(col_placement[:row])):
