#37. Sudoku Solver
#Write a program to solve a Sudoku puzzle by filling the empty cells.

#A sudoku solution must satisfy all of the following rules:

#Each of the digits 1-9 must occur exactly once in each row.
#Each of the digits 1-9 must occur exactly once in each column.
#Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
#The '.' character indicates empty cells.


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        ##backtracking
        
        ## we need collect options for each row, column and each 3*3 area
        row_opt= [set([str(i) for i in range(1, 10)]) for _ in range(9)]
        col_opt=[set([str(i) for i in range(1, 10)]) for _ in range(9)]
        thr_thr_opt= [[set([str(i) for i in range(1, 10)]) for _ in range(3)] for _ in range(3)]
        for row in range(9):
            for col in range(9):
                if board[row][col]!='.':
                    row_opt[row].remove(board[row][col])
                    col_opt[col].remove(board[row][col])
                    thr_thr_opt[row//3][col//3].remove(board[row][col])
                    
        ##backtrack
        self.out=None
        
        def backtrack(board, row_i, col_i, row_opt, col_opt, thr_thr_opt):
            ##bottom case:            
            if row_i==9:
                return board
            elif col_i==9:
                return backtrack(board, row_i+1, 0, row_opt, col_opt, thr_thr_opt)
            elif board[row_i][col_i]!='.':
                return backtrack(board, row_i, col_i+1, row_opt, col_opt, thr_thr_opt)
            else:
                available=list(row_opt[row_i] & col_opt[col_i] & thr_thr_opt[row_i//3][col_i//3])
                for candidate in available:
                    board[row_i][col_i]=candidate
                    row_opt[row_i].remove(candidate)
                    col_opt[col_i].remove(candidate)
                    thr_thr_opt[row_i//3][col_i//3].remove(candidate)
                    out=backtrack(board, row_i, col_i+1, row_opt, col_opt, thr_thr_opt)
                    if out: return out
                    board[row_i][col_i]='.'
                    row_opt[row_i].add(candidate)
                    col_opt[col_i].add(candidate)
                    thr_thr_opt[row_i//3][col_i//3].add(candidate)   
            return None
        
        board= backtrack(board, 0, 0, row_opt, col_opt, thr_thr_opt)
        
        
        