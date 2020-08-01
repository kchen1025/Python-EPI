from test_framework import generic_test


def number_of_ways(n: int, m: int) -> int:
    memo = [[0 for j in range(m)] for i in range(n)]


    def traverse(i,j):
        if i == 0 or j == 0: return 1
        if memo[i][j]: return memo[i][j]

        memo[i][j] = traverse(i-1,j) + traverse(i,j-1)
        return memo[i][j]

    return traverse(n-1, m-1)


if __name__ == '__main__':
    # print(number_of_ways(3,3))
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))




































# def number_of_ways(n: int, m: int) -> int:
#     memo = [[0 for i in range(n)] for j in range(m)]
#
#     memo[0] = [1 for i in range(n)]
#
#     for i in range(m):
#         memo[i][0] = 1
#
#     for i in range(1,m):
#         for j in range(1,n):
#             memo[i][j] = memo[i-1][j]+ memo[i][j-1]
#     return memo[-1][-1]


# ways = [[0 for i in range(n)] for j in range(m)]
#
#     def num_ways(x, y):
#         if ways[x][y] != 0:
#             return ways[x][y]
#
#         if x == 0 or y == 0:
#             ways[x][y] = 1
#             return 1
#
#         ways[x][y] = num_ways(x-1,y) + num_ways(x,y-1)
#         return ways[x][y]
#
#     return num_ways(m-1,n-1)
