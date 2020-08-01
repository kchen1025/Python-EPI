import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def getDepth(node):
    if not node:
        return -1

    curr = node
    depth = 0
    while curr.parent:
        curr = curr.parent
        depth +=1
    return depth

def lca(node1: BinaryTreeNode,
        node2: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if not node1 or not node2: return None

    depth1 = getDepth(node1)
    depth2 = getDepth(node2)

    # take deeper of 2 nodes and traverse down
    # set node1 to always be deepest
    if depth2 > depth1:
        node1,node2 = node2,node1
        depth1,depth2 = depth2,depth1

    # set node1 to same depth
    for _ in range(depth1 - depth2):
        node1 = node1.parent

    while node1 and node2 and node1 != node2:
        node1 = node1.parent
        node2 = node2.parent

    return node1



@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
