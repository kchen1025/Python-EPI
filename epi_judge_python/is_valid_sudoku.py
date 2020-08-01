from typing import List

from test_framework import generic_test

import math

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    # check row and columns
    n = len(partial_assignment)
    # if any(
    #     has_duplicate([partial_assignment[i][j] for i in range(n)]) or
    #     has_duplicate([partial_assignment[j][i] for i in range(n)])
    #     for j in range(n)
    # ):
    #     return False

    # check boxes

    region_size = int(math.sqrt(n))
    a = [
        partial_assignment[a][b]
        for a in range(region_size * I, region_size * (I+1))
        for b in range(region_size * J, region_size * (J+1))
    ]
    print(a)


    return True

if __name__ == '__main__':
    print(is_valid_sudoku([
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 2, 0, 0],
        [0, 0, 0, 0, 6, 0, 4, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 5],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 3, 0],
        [0, 0, 4, 0, 0, 0, 0, 0, 0]
    ]))

    # exit(
    #     generic_test.generic_test_main('is_valid_sudoku.py',
    #                                    'is_valid_sudoku.tsv', is_valid_sudoku))
