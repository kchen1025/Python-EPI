from typing import List

from test_framework import generic_test

import math
def minimum_path_weight(triangle: List[List[int]]) -> int:
    memo = [[None for j in range(len(i))] for i in triangle]

    if not triangle: return 0
    def traverse(i,j):
        if i == 0: return triangle[0][0]
        if i < 0 or j < 0 or i >= len(triangle) or j >= len(triangle[i]): return math.inf
        if memo[i][j] != None: return memo[i][j]

        memo[i][j] = min(traverse(i-1,j-1), traverse(i-1,j)) + triangle[i][j]
        return memo[i][j]

    minVal = math.inf
    for i in range(len(triangle[-1])):
        minVal = min(minVal, traverse(len(triangle)-1, i))
    return minVal

if __name__ == '__main__':
    # print(minimum_path_weight([[1],[2,3],[4,5,6],[7,8,9,10]]))
    # print(minimum_path_weight([[2],[4,4],[8,5,6],[4,2,6,2],[1,5,2,3,4]]))
    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
