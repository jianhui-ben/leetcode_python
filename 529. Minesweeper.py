#529. Minesweeper https://leetcode.com/problems/minesweeper/
#Let's play the minesweeper game (Wikipedia, online game)!

#You are given an m x n char matrix board representing the game board where:

#'M' represents an unrevealed mine,
#'E' represents an unrevealed empty square,
#'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
#digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
#'X' represents a revealed mine.
#You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

#Return the board after revealing this position according to the following rules:

#If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
#If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
#If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
#Return the board when no more squares will be revealed.

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """
        two steps:
        - update reveal or not (dfs)
        - update the number on the board
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        
        mines = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'M':
                    mines.add((r, c))
        
        def dfs_reveal(board, mines, r, c):
            if 0 <=r < len(board) and 0<=c<len(board[0]):
                if board[r][c] == 'E':
                    d = [(0, 1), (0, -1), (1, 0), (-1, 0), \
                         (1, 1), (1, -1), (-1, 1), (-1, -1)]
                    cnt = 0
                    for d_r, d_c in d:
                        new_r, new_c = r+d_r, c+d_c
                        if (new_r, new_c) in mines:
                            cnt += 1
                    if not cnt:
                        board[r][c] = 'B'
                        for d_r, d_c in d:
                            new_r, new_c = r+d_r, c+d_c
                            dfs_reveal(board, mines, new_r, new_c)
                    else:
                        board[r][c] = str(cnt)
        
        
        dfs_reveal(board, mines, click[0], click[1])
        return board
        
        