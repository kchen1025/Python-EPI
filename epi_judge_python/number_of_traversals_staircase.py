from test_framework import generic_test


def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    memo = [0 for i in range(top+1)]

    def traverse(n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if memo[n]:
            return memo[n]

        for i in range(1, maximum_step+1):
            memo[n] += traverse(n-i)

        return memo[n]
    return traverse(top)





if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_staircase.py',
                                       'number_of_traversals_staircase.tsv',
                                       number_of_ways_to_top))
