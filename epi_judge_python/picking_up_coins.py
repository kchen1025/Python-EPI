from typing import List

from test_framework import generic_test

import math

def maximum_revenue(coins: List[int]) -> int:
    memo = [[None for j in range(len(coins))] for i in range(len(coins))]

    def pick(start,end):
        if start > end:
            return 0
        if memo[start][end] != None:
            return memo[start][end]

        front = coins[start] + min(pick(start+2, end), pick(start+1, end-1))
        back = coins[end] + min(pick(start,end-2),pick(start+1,end-1))

        memo[start][end] = max(front,back)
        return memo[start][end]
    return pick(0,len(coins)-1)        


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
