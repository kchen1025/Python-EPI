import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

directions = [[-1, 0],[0, 1],[1,0],[0,-1]] # up, right, down, left

NOT_VISITED = 1
VISITING = 2
VISITED = 3

def oob(i,j,maze):
    if i < 0 or j < 0 or i >= len(maze) or j >= len(maze[0]):
        return True
    return False

def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    def build_graph():
        # loop through all elements
        # if its a space, loop through all directions and add to adj list
        graph = collections.defaultdict(list)
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == WHITE:
                    for dir in directions:
                        new_i = i+dir[0]
                        new_j = j+dir[1]
                        if not oob(new_i,new_j,maze) and maze[new_i][new_j] == WHITE:
                            graph[(i,j)].append((new_i,new_j))
        return graph

    # dfs
    coords = []
    def hasPath(start,end,visited=set()):
        start = tuple(start)
        end = tuple(end)
        if start in visited:
            return False
        if start == end:
            coords.append(Coordinate(start[0],start[1]))
            return True

        # visit current node
        visited.add(start)
        coords.append(Coordinate(start[0],start[1]))
        # loop through neighbors and visit
        for node in graph[start]:
            if node not in visited and hasPath(node,end,visited):
                return True
        coords.pop()
        return False



    graph = build_graph()
    if hasPath(s,e):
        return coords
    return []
































    # # create tracking maze
    # memo = [[NOT_VISITED for j in maze[0]] for i in maze]
    # output = []
    #
    # def findPath(i,j):
    #     if i == e.x and j == e.y:
    #         output.append(Coordinate(i,j))
    #         return True
    #
    #     #invalid spaces
    #     if oob(i,j,maze) or memo[i][j] != NOT_VISITED or maze[i][j] == BLACK:
    #         return False
    #
    #     memo[i][j] = VISITING
    #     output.append(Coordinate(i,j))
    #
    #     for dir in DIRECTIONS:
    #         new_i = i + dir[0]
    #         new_j = j + dir[1]
    #         if findPath(new_i,new_j):
    #             return True
    #
    #     # remove from output because not valid space
    #     output.pop()
    #     return False
    #
    # if findPath(s.x, s.y):
    #     return output
    # return []


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':    
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
