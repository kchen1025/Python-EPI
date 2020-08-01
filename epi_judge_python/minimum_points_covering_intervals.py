import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def find_minimum_visits(intervals: List[Interval]) -> int:
    if not intervals: return 0

    # sort by ending point
    intervals.sort(key=lambda x:x.right)

    count = 1
    currentVisit = intervals[0].right

    for i in range(1, len(intervals)):
        if intervals[i].left > currentVisit:
            count+=1
            currentVisit = intervals[i].right
    return count






































    # if not intervals: return 0
    # # first sort by right endpoints
    # intervals.sort(key=lambda x:x.right)
    #
    # output = 1
    # overlap = intervals[0].right
    # # the first interval to end's rightmost point must be in the output
    # for i in range(1,len(intervals)):
    #     # if our overlap is not in interval, increase our count, and set the new rightmost point to our overlap
    #     if intervals[i].left > overlap:
    #         output += 1
    #         overlap = intervals[i].right
    # return output
    #


@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    # print(find_minimum_visits([Interval(0,3), Interval(2,6), Interval(3,4), Interval(6,9)]))
    exit(
        generic_test.generic_test_main(
            'minimum_points_covering_intervals.py',
            'minimum_points_covering_intervals.tsv',
            find_minimum_visits_wrapper))
