from typing import List
from test_framework import generic_test
import collections

directions = [[-1, 0],[0, 1],[1,0],[0,-1]] # up, right, down, left

Coordinate = collections.namedtuple('Coordinate', ('x','y'))

def oob(x,y,image):
    if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]):
        return True
    return False

def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    queue = collections.deque([[x,y]])
    color = image[x][y]
    visited = set()
    visited.add(tuple([x,y]))

    # begin at start, add adjacent elems to queue and flip our current one. do this until we have no more in the queue
    while queue:
        visiting = queue.popleft()

        # flip color
        image[visiting[0]][visiting[1]] = not color

        # look at neighors
        for dir in directions:
            new_x = visiting[0] + dir[0]
            new_y = visiting[1] + dir[1]
            new_cell = [new_x,new_y]

            if not oob(new_x,new_y,image) and image[new_x][new_y] == color and tuple(new_cell) not in visited:
                visited.add(tuple(new_cell))
                queue.append(new_cell)

    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    # yeet = [[True,True,True,True,False],[True,True,True,False,True],[False,False,False,True,True],[True,True,False,True,True],[True,False,True,True,True]]
    # flip_color_wrapper(2,3,yeet)
    # print(yeet)
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
