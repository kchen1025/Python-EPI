from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

import collections

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree: return []
    out = []

    queue = collections.deque([tree])

    while queue:
        out.append([i.data for i in queue])

        length = len(queue)

        for i in range(length):
            visiting = queue.popleft()
            if visiting.left: queue.append(visiting.left)
            if visiting.right: queue.append(visiting.right)

    return out




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
