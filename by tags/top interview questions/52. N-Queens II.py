#52. N-Queens II
#The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

#Given an integer n, return the number of distinct solutions to the n-queens puzzle.


class Solution:
    def totalNQueens(self, n: int) -> int:
        template=[[0]* n for _ in range(n)]
        out=0 
        
        def update(template, row, col):
            for i in range(n):
                for j in range(n):
                    if i==row or j==col or i+j==row+col or i-j==row-col:
                        template[i][j]=1
            return template
        
        
        def backtrack(row, template):

            if row==n:
                out+=1
            else:
                for col in range(n):
                    if template[row][col]==0:
                        old_template= [[n for n in m] for m in template]
                        new_template= update(template, row, col)
                        backtrack(row+1, new_template)
                        template=old_template
            
        backtrack(0, template)
        return out