from typing import Optional

from bst_node import BstNode
from test_framework import generic_test

import math

def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    runner, first_so_far = tree, None

    while runner:
        if k < runner.data:
            first_so_far = runner
            runner = runner.left
        else:
            runner = runner.right
    return first_so_far

    # parent = None
    #
    # def traverse(node):
    #     nonlocal parent
    #
    #     if not node:
    #         return parent
    #
    #     if node.data < k:
    #         return traverse(node.right)
    #     elif node.data > k:
    #         parent = node
    #         return traverse(node.left)
    #     else:
    #         if node.right:
    #             return getLeft(node.right)
    #         else:
    #             return parent
    #
    # def getLeft(node):
    #     if not node:
    #         return None
    #     if node.left:
    #         return getLeft(node.left)
    #     return node
    #
    # return traverse(tree)


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
