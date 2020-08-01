from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import namedtuple

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def dfs(node):
        if not node:
            return (True, -1)

        leftBal, leftHeight = dfs(node.left)
        rightBal, rightHeight = dfs(node.right)

        return (leftBal and rightBal and abs(leftHeight-rightHeight) <= 1, max(leftHeight,rightHeight) + 1)
    return dfs(tree)[0]


if __name__ == '__main__':
    one = BinaryTreeNode(1)
    two = BinaryTreeNode(2)
    three = BinaryTreeNode(3)
    four = BinaryTreeNode(4)
    five = BinaryTreeNode(5)
    six = BinaryTreeNode(6)

    one.left = two
    one.right = three

    two.right = four
    three.left = five
    four.right = six

    # print(is_balanced_binary_tree(one))
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
