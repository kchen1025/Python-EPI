from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(matrix: List[List[int]]) -> List[int]:
    L = len(matrix)
    n = len(matrix)-1
    out = []
    for layer in range(L//2):
        #top
        for i in range(n - (2*layer)):
            out.append(matrix[layer][layer+i])
        #right
        for i in range(n - (2*layer)):
            out.append(matrix[i+layer][n-layer])
        #bottom
        for i in range(n - (2*layer)):
            out.append(matrix[n-layer][n-i-layer])
        #left
        for i in range(n - (2*layer)):
            out.append(matrix[n-i-layer][layer])
    # edge case for odd
    if L % 2 == 1: out.append(matrix[L//2][L//2])

    return out

if __name__ == '__main__':
    # print(matrix_in_spiral_order([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))

    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
