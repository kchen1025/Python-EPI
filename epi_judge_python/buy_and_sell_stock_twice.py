from typing import List

from test_framework import generic_test

import math

def buy_and_sell_stock_twice(arr: List[float]) -> float:
    best_till_i = [0]*len(arr)
    best_from_i = [0]*len(arr)
    min_so_far = math.inf
    max_from_back = -math.inf
    best_trade = -math.inf

    for i,elem in enumerate(arr):
        min_so_far = min(min_so_far, elem)
        best_trade = max(best_trade, elem-min_so_far)
        best_till_i[i] = best_trade

    best_trade = -math.inf
    for i,elem in reversed(list(enumerate(arr))):
        max_from_back = max(max_from_back, elem)
        best_trade = max(best_trade, max_from_back - elem)
        best_from_i[i] = best_trade
    max2 = -math.inf
    for i in range(len(arr) - 1):
        max2 = max(max2, best_till_i[i] + best_from_i[i+1])
    return max(max2, best_till_i[-1])




if __name__ == '__main__':

    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
