#1277. Count Square Submatrices with All Ones

#Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

#Example 1:

#Input: matrix =
#[
#  [0,1,1,1],
#  [1,1,1,1],
#  [0,1,1,1]
#]
#Output: 15
#Explanation: 
#There are 10 squares of side 1.
#There are 4 squares of side 2.
#There is  1 square of side 3.
#Total number of squares = 10 + 4 + 1 = 15.

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        [
            [1,0,1],
            [1,1,0],
            [1,1,0]
        ]
        
        [1, 1, 2],
        [2, 3, 4],
        [3, 5, 6]
        
        dp: check lt 221
        """
        out = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row > 0 and col > 0:
                    if matrix[row][col] == 1:
                        matrix[row][col] = 1 + min(matrix[row -1][col - 1], \
                                                  matrix[row][col - 1], \
                                                  matrix[row - 1][col])
                
                out += matrix[row][col]
        return out
        
        
        