from typing import List

from test_framework import generic_test

import math
import collections


def buy_and_sell_stock_once(prices):
    best_trade = -math.inf
    min_so_far = math.inf

    for price in prices:
        min_so_far = min(min_so_far, price)
        best_trade = max(best_trade,price - min_so_far)


    return best_trade


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
