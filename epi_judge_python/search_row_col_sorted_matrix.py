from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:
    # loop from bottom to top
    i,j = len(A)-1,0

    while i >= 0 and j < len(A[0]):
        if A[i][j] == x:
            return True

        # if x is less, go up row
        if x < A[i][j]:
            i -= 1

        # if x is greater, go right row
        if x > A[i][j]:
            j += 1
    
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
