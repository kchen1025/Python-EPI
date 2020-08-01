from typing import List

from test_framework import generic_test
import functools

directions = [[-1,0],[0,1],[1,0],[0,-1]] # up right down left

def oob(i,j,grid):
    if i<0 or i>= len(grid) or j<0 or j>=len(grid[0]): return True
    return False


def is_pattern_contained_in_grid(grid: List[List[int]], pattern: List[int]) -> bool:
    memo = [[[True for j in range(len(grid[0]))] for i in range(len(grid))] for k in range(len(pattern))]

    def hasPath(i,j,startIdx):
        if startIdx >= len(pattern):
            return True
        if oob(i,j,grid): return False        
        if grid[i][j] != pattern[startIdx]: return False
        if memo[startIdx][i][j] == False: return False

        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            if hasPath(new_i, new_j, startIdx+1): return True

        memo[startIdx][i][j] = False
        return False

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if hasPath(i,j,0): return True
    return False


































    # memo = [[[False for j in range(len(grid[0]))] for i in range(len(grid))] for k in range(len(pattern))]
    #
    # def patternExists(i,j,offset=0):
    #     if offset == len(pattern): return True
    #     if oob(i,j,grid): return False
    #     if memo[offset][i][j]: return False
    #     if grid[i][j] != pattern[offset]: return False
    #
    #     for dir in directions:
    #         new_i,new_j = i+dir[0],j+dir[1]
    #         if patternExists(new_i,new_j,offset+1):
    #             return True
    #     memo[offset][i][j] = True
    #     return False
    #
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if patternExists(i,j):
    #             return True
    # return False

# def is_pattern_contained_in_grid(grid: List[List[int]], pattern: List[int]) -> bool:
#     @functools.lru_cache(None)
#     def is_pattern(x,y,offset):
#         if len(pattern) == offset:
#             return True
#         if (not (0 <= x < len(grid) and 0 <= y < len(grid[x])) or grid[x][y] != pattern[offset]):
#             return False
#         return any(is_pattern(*next_xy, offset+1) for next_xy in ((x-1, y), (x+1, y), (x,y-1), (x,y+1)))
#     return any(is_pattern(i,j,offset=0) for i in range(len(grid)) for j in range(len(grid[i])))
#





if __name__ == '__main__':
    # print(is_pattern_contained_in_grid([[1,2,3],[3,4,5],[5,6,7]], [1,3,4,6]))
    # print(is_pattern_contained_in_grid([[1,2,3],[3,4,5],[5,6,7]], [1,2,3,4]))
    # print(is_pattern_contained_in_grid([[39, 39, 39, 39], [39, 39, 39, 39], [39, 39, 39, 39]], [39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 38]))
    # print(is_pattern_contained_in_grid([[21,7,7],[7,7,7],[9,21,25]], [7,7,9]))

    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
