from typing import List

from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    if not A: return 0

    memo = [1] + [0 for i in range(len(A)-1)]

    maxSequence = 1
    for i in range(1,len(A)):
        # look for greatest val less than i
        for j in reversed(range(i)):
            if A[i] >= A[j]:
                memo[i] = max(memo[i], memo[j]+1)
            memo[i] = max(memo[i], 1)

        maxSequence = max(maxSequence, memo[i])
    return maxSequence




if __name__ == '__main__':
    print(longest_nondecreasing_subsequence_length([1,3,5,4,7]))
    # exit(
    #     generic_test.generic_test_main(
    #         'longest_nondecreasing_subsequence.py',
    #         'longest_nondecreasing_subsequence.tsv',
    #         longest_nondecreasing_subsequence_length))
