from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    buff = []
    output = []

    def helper(startIdx):
        output.append(buff.copy())
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
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
