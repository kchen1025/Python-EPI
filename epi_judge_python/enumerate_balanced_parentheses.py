from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    out = []
    buff = []

    def helper(leftParen, rightParen):
        if leftParen == num_pairs and rightParen == num_pairs:
            out.append(''.join(buff))
            return

        if leftParen <= num_pairs:
            buff.append('(')
            helper(leftParen + 1, rightParen)
            buff.pop()

        if rightParen < leftParen:
            buff.append(')')
            helper(leftParen, rightParen+1)
            buff.pop()
    helper(0,0)
    return out


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
