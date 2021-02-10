#51. N-Queens
#The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

#Given an integer n, return all distinct solutions to the n-queens puzzle.

#Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ## backtracking
        template= [[0]*n for _ in range(n)]
        self.out= []
        
        def update(template, row, col):
            new_template= [[n for n in m] for m in template]
            for j in range(n):
                for k in range(n):
                    if j==row or k==col or j+k==row+col or j-k==row-col:
                        new_template[j][k]=1
            return new_template
        
        def backtrack(row, template, cur):
            if row==n:
                self.out.append(cur)
            else:
                for col in range(n):
                    if template[row][col]==0:
                        new_template=update(template, row, col)
                        backtrack(row+1, new_template, \
                                  cur+[''.join(['Q' if i==col else '.' for i in range(n)])])

        backtrack(0, template, [])
        return self.out