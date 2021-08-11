#562. Longest Line of Consecutive One in Matrix

#Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.

#The line could be horizontal, vertical, diagonal, or anti-diagonal.

 

#Example 1:


#Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
#Output: 3
#Example 2:


#Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
#Output: 4

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        """
        dp[i][j] = (left, upperleft, up, uppper right)
        
        add an outer bound of 0s
        
        time: row * col
        space: row * col * 4, can do further space compression
        """
        out = 0
        dp = [[(0, 0, 0, 0) for _ in range(len(mat[0]) + 2)] for _ in range(len(mat) + 2)]
                
        for row in range(1, len(dp) - 1):
            for col in range(1, len(dp[0]) - 1):
                if mat[row - 1][col - 1] == 1:
                    dp[row][col] = (dp[row][col - 1][0] + 1, dp[row-1][col-1][1] + 1,\
                                   dp[row-1][col][2] + 1, dp[row-1][col+1][3] + 1)
                    
                    out = max(out, max(dp[row][col]))
        
        return out
                    
