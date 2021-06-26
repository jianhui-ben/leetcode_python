#36. Valid Sudoku
#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#Note:

#A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#Only the filled cells need to be validated according to the mentioned rules.
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        3 hashtables:
        row_level = [set()] * 9
        col_level = [set()] * 9
        
        0 1 2
        3 4 5
        6 7 8
        
        sub_box_level = [set()] * 9
        
        (row // 3) + (col // 3) = index in sub_box_level 
        
        for every single board[row][col]:
          we check if corresponding 3 hashtables have it:
          -- yes: return False
          -- No: add and continue
        """
        row_level, col_level, sub_box_level = [set() for _ in range(9)],\
        [set() for _ in range(9)], [set() for _ in range(9)]
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != '.':
                    num = int(board[row][col])
                    if num in row_level[row] or num in col_level[col] \
                    or num in sub_box_level[(row // 3) * 3 + (col // 3)]:
                        return False
                    row_level[row].add(num)
                    col_level[col].add(num)
                    sub_box_level[(row // 3) * 3 + (col // 3)].add(num)
                    
        return True