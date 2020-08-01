from test_framework import generic_test
import functools


def compute_binomial_coefficient(n: int, k: int) -> int:
    memo = [[None for j in range(k+1)] for i in range(n+1)]

    def recurse(n, k):
        if k == 0:
            return 1
        if n == 0:
            return 0

        if memo[n][k] != None:
            return memo[n][k]

        memo[n][k] = recurse(n-1,k) + recurse(n-1,k-1)
        return memo[n][k]

    yeet = recurse(n,k)
    return yeet
#
#
# memo = [[None]*(n+1) for _ in range(k+1)]
# def recurse(n, k):
#     if k == 0:
#         return 1
#     if n == 0:
#         return 0
#     if memo[k][n] != None:
#         return memo[k][n]
#
#     memo[k][n] = recurse(n-1, k) + recurse(n-1, k-1)
#     return memo[k][n]
#
# return recurse(n,k)






































# def compute_binomial_coefficient(n: int, k: int) -> int:
#     limit = n-k
#     count = k
#     output = 1
#
#     for i in range(n, limit, -1):
#         output *= (i/count)
#         count-=1
#     return output

# @functools.lru_cache(None)
# def compute_binomial_coefficient(n,k):
#     print('call')
#     if k in (0,n):
#         return 1
#
#     without_k = compute_binomial_coefficient(n-1,k)
#     with_k = compute_binomial_coefficient(n-1,k-1)
#     return without_k + with_k




# def compute_binomial_coefficient(n: int, k: int) -> int:
    # C = [[0 for x in range(k+1)] for x in range(n+1)]
    #
    # # Calculate value of Binomial Coefficient in bottom up manner
    # for i in range(n+1):
    #     for j in range(min(i, k)+1):
    #         # Base Cases
    #         if j == 0 or j == i:
    #             C[i][j] = 1
    #
    #         # Calculate value using previously stored values
    #         else:
    #             C[i][j] = C[i-1][j-1] + C[i-1][j]
    #
    # return C[n][k]



if __name__ == '__main__':
    # print(compute_binomial_coefficient(1,0))
    # print(compute_binomial_coefficient(10,2))

    exit(
        generic_test.generic_test_main('binomial_coefficients.py',
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
