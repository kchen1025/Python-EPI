import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

NOT_VISITED, VISITING, VISITED = 1,2,3

class GraphVertex:
    def __init__(self) -> None:
        self.edges: List['GraphVertex'] = []
        self.state = NOT_VISITED


def is_deadlocked(graph: List[GraphVertex]) -> bool:
    def hasCycle(node):
        if not node or node.state == VISITED:
            return False

        if node.state == VISITING:
            return True

        node.state = VISITING
        for edge in node.edges:
            if hasCycle(edge): return True

        node.state = VISITED
        return False


    # loop through each vertex in the graph
    # if not visited, checkCycle
    for node in graph:
        if node.state == NOT_VISITED and hasCycle(node):
            return True
    return False




@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('deadlock_detection.py',
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))
