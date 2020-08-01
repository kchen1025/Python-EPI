from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

import math

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:

    def isBST(node, min=-math.inf, max=math.inf):
        if not node:
            return True

        return min <= node.data <= max and isBST(node.left, min, node.data) and isBST(node.right, node.data, max)

    return isBST(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
