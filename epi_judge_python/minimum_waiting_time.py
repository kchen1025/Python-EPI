from typing import List

from test_framework import generic_test


def minimum_total_waiting_time(service_times: List[int]) -> int:
    service_times.sort()

    currSum = 0
    totalWait = 0

    for i in service_times:
        totalWait += currSum
        currSum += i
    return totalWait



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_waiting_time.py',
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
