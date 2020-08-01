from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    out = []
    count = 0

    def traverse(node):
        nonlocal count

        if not node:
            return

        traverse(node.right)

        if count == k: return
        out.append(node.data)
        count+=1

        traverse(node.left)

    traverse(tree)
    return out




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
