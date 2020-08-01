from typing import List

from test_framework import generic_test
import math

def get_max_trapped_water(heights: List[int]) -> int:
    start,end = 0, len(heights)-1

    maxTrapped = -math.inf

    while start < end:
        maxTrapped = max(maxTrapped, min(heights[start],heights[end])*(end-start))
        if heights[start] < heights[end]:
            start+=1
        else:
            end-=1
    return maxTrapped


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
