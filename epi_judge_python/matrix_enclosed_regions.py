from typing import List

from test_framework import generic_test

directions = [[-1, 0],[0, 1],[1,0],[0,-1]] # up, right, down, left

def oob(x,y,image):
    if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]):
        return True
    return False

SPEC = 'S'
def fill_surrounded_regions(board: List[List[str]]) -> None:    
    # loop along border, if a space is a white, do a dfs until you have no more spaces and mark those all as
    # special
    # then loop through all elements on the board and flip the special chars to whites, and flip the whites to blacks
    visited = set()

    def dfs(i,j):
        if oob(i,j,board) or (i,j) in visited or board[i][j] != 'W':
            return
        # visit by setting char to special
        board[i][j] = SPEC
        visited.add((i,j))
        # loop all directions
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]
            dfs(new_i,new_j)

    # loop top and bottom
    for j in range(len(board[0])):
        if board[0][j] == 'W': dfs(0,j)
        if board[len(board)-1][j] == 'W': dfs(len(board)-1,j)

    # left and right, skipping top and bottom because already done
    for i in range(1,len(board)-1):
        if board[i][0] == 'W': dfs(i,0)
        if board[i][len(board[0])-1] == 'W': dfs(i,len(board[0])-1)

    # done, flip all pieces
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'W':
                board[i][j] = 'B'
            elif board[i][j] == SPEC:
                board[i][j] = 'W'
    return




def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    # yeet = [['B','B','B','W','W'],['W','B','W','B','W'],['W','B','B','W','B'],['W','W','B','B','B'],['W','W','W','W','W']]
    # fill_surrounded_regions(yeet)
    # print(yeet)

    fill_surrounded_regions([
    ["W", "W", "W", "W", "B", "W", "W", "B", "B", "W"],
    ["B", "W", "W", "B", "W", "B", "W", "B", "B", "W"],
    ["B", "W", "W", "W", "B", "B", "B", "B", "B", "W"],
     ["B", "B", "B", "B", "W", "B", "W", "B", "W", "B"],
     ["W", "W", "B", "B", "W", "B", "B", "W", "B", "B"],
      ["W", "W", "W", "B", "B", "B", "B", "W", "W", "W"],
      ["B", "B", "W", "B", "W", "B", "B", "W", "W", "B"],
      ["B", "W", "W", "W", "B", "W", "B", "W", "B", "W"],
      ["W", "W", "W", "W", "B", "W", "W", "W", "B", "B"],
      ["W", "W", "W", "W", "B", "B", "W", "B", "B", "B"],
      ["B", "B", "W", "B", "B", "B", "W", "B", "W", "B"],
      ["B", "W", "W", "B", "B", "B", "W", "W", "B", "B"],
      ["B", "B", "W", "B", "W", "W", "B", "W", "W", "B"],
      ["B", "B", "B", "W", "B", "B", "B", "B", "W", "W"],
      ["W", "B", "W", "B", "B", "B", "W", "B", "B", "B"]])

    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
