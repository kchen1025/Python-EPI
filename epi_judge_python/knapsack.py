import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))

def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    memo = [[None for j in range(capacity+1)] for i in range(len(items))]

    def traverse(i,j):
        if i < 0 or j < 0: return 0
        if memo[i][j] != None: return memo[i][j]

        memo[i][j] = max(traverse(i-1, j), items[i].value + traverse(i-1,j - items[i].weight)) if (j - items[i].weight) >= 0 else traverse(i-1, j)
        return memo[i][j]

    yeet = traverse(len(items)-1, capacity)
    return yeet


































    # @functools.lru_cache(None)
    # def opt(k, available_capacity):
    #     if k < 0:
    #         return 0
    #     without_curr = opt(k-1, available_capacity)
    #     with_curr = (0 if available_capacity < items[k].weight else (items[k].value + opt(k-1, available_capacity - items[k].weight)))
    #
    #     return max(without_curr, with_curr)
    # return opt(len(items)-1, capacity)

# def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
#     memo = [[0 for j in range(capacity+1)] for i in range(len(items))]
#
#     def getVal(i,j):
#         if i < 0: return 0
#         if j < 0: return 0
#         if i == 0:
#             if (j - items[i].weight) >= 0:
#                 return items[i].value
#             else:
#                 return 0
#
#         if memo[i][j]: return memo[i][j]
#
#         without_curr = getVal(i-1,j)
#         with_curr = items[i].value + getVal(i-1, j - items[i].weight) if items[i].weight <= j else 0
#         memo[i][j] = max(without_curr, with_curr)
#         return memo[i][j]
#
#
#     yeet = getVal(len(items)-1, capacity)
#     return yeet



@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    items = [Item(5,60),Item(3,50),Item(4,70),Item(2,30)]
    print(optimum_subject_to_capacity(items, 5))


    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))












#
#
#
# def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
#     memo = [[None for i in range(capacity+1)] for j in items]
#
#     def calcMax(itemIdx, cap):
#         if itemIdx < 0:
#             return 0
#
#         if memo[itemIdx][cap] is not None:
#             return memo[itemIdx][cap]
#
#
#         if items[itemIdx].weight > cap:
#             return calcMax(itemIdx-1, cap)
#
#
#         memo[itemIdx][cap] = max(
#             calcMax(itemIdx-1, cap),
#             calcMax(itemIdx-1, cap - items[itemIdx].weight) + items[itemIdx].value
#         )
#         return memo[itemIdx][cap]
#
#     return calcMax(len(items)-1,capacity)






    #
    # memo = [[None for i in range(capacity + 1)] for j in range(len(items))]
    #
    # def getMax(itemIdx, weight):
    #     if itemIdx < 0:
    #         return 0
    #     # # if itemIdx < 0 or weight < 0:
    #     # #     return 0
    #     #
    #     # if itemIdx == 0:
    #     #     if items[itemIdx].weight < weight:
    #     #         return 0
    #     #     else:
    #     #         return items[itemIdx].value
    #     #
    #     # if weight == 0:
    #     #     return 0
    #     #
    #     if memo[itemIdx][weight] is not None:
    #         return memo[itemIdx][weight]
    #
    #     weight_without = getMax(itemIdx - 1, weight)
    #     weight_with = 0 if items[itemIdx].weight > weight else (getMax(itemIdx-1, weight-items[itemIdx].weight) + items[itemIdx].value)
    #
    #     memo[itemIdx][weight] = max(weight_with, weight_without)
    #     return memo[itemIdx][weight]
    #
    # return getMax(len(items)-1, capacity)






    #
    #
    #
    #
    #
    #
    # memo = [[0 for i in range(len(items))] for j in range(len(items))]
    #
    # def optimum_subject_to_item_and_capacity(k, available_capacity):
    #     if k < 0:
    #         return 0
    #
    #     without_curr_item = optimum_subject_to_item_and_capacity(k-1, available_capacity)
    #     with_curr_item = (0 if available_capacity < items[k].weight else (items[k].value + optimum_subject_to_item_and_capacity(k-1, available_capacity - items[k].weight)))
    #     return max(without_curr_item, with_curr_item)
    # return optimum_subject_to_item_and_capacity(len(items)-1, capacity)
