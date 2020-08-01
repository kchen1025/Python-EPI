from typing import List

from test_framework import generic_test

def generate_pascal_triangle(n: int) -> List[List[int]]:
    out = [[1] * (i+1) for i in range(n)]

    for i in range(n):
        for j in range(1, i):
            out[i][j] = out[i-1][j] + out[i-1][j-1]
    return out


# def generate_pascal_triangle(n: int) -> List[List[int]]:
#     base = [[1],[1,1]]
#
#     if n <= 2:
#         return base[0:n]
#
#     base.extend([[1] for i in range(n-2)])
#
#     for i in range(2, len(base)):
#         for j in range(1, len(base[i-1])):
#             base[i].append(base[i-1][j] + base[i-1][j-1])
#         base[i].append(1)
#     return base


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
