from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    buff = []
    isInBuff = [False]*len(A)
    output = []

    def permHelper(start):
        if start >= len(A):
            output.append(buff.copy())
            return

        for i in range(len(A)):
            if not isInBuff[i]:
                isInBuff[i] = True
                buff.append(A[i])
                permHelper(start+1)
                isInBuff[i] = False
                buff.pop()
    permHelper(0)
    return output


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
