from typing import List

from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:
    input_set = [i for i in range(1,n+1)]
    buff = []
    output = []

    def helper(startIdx):
        if len(buff) == k:
            output.append(buff.copy())
            return

        if startIdx >= len(input_set):
            return

        for i in range(startIdx, len(input_set)):
            buff.append(input_set[i])
            helper(i+1)
            buff.pop()

    helper(0)
    return output



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
