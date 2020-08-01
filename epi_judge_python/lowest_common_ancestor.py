import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(root: BinaryTreeNode, node1: BinaryTreeNode,
        node2: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if not root: return
    if node1 == root or node2 == root: return root

    leftLCA = lca(root.left, node1, node2)
    rightLCA = lca(root.right, node1, node2)

    if leftLCA and rightLCA:
        return root
    if leftLCA:
        return leftLCA
    if rightLCA:
        return rightLCA
    return None


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
