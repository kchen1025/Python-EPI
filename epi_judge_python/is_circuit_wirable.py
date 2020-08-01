import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
import collections

class GraphVertex:
    def __init__(self) -> None:
        self.d = -1
        self.edges: List[GraphVertex] = []
        self.depth = None

def is_any_placement_feasible(graph: List[GraphVertex]) -> bool:
    if not graph: return False    

    for node in graph:
        if node.depth == None and not checkBipartite(node):
            return False
    return True

def checkBipartite(graphNode):
    graphNode.depth = 1
    queue = collections.deque([graphNode])

    while queue:
        visiting = queue.popleft()

        # visit neighbors
        for node in visiting.edges:
            if node.depth == None:
                node.depth = visiting.depth+1
                queue.append(node)
            elif node.depth == visiting.depth:
                return False
    return True




@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])
    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_circuit_wirable.py',
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
