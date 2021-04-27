#931. Minimum Falling Path Sum
#Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

#A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

#Example 1:

#Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
#Output: 13
#Explanation: There are two falling paths with a minimum sum underlined below:
#[[2,1,3],      [[2,1,3],
# [6,5,4],       [6,5,4],
# [7,8,9]]       [7,8,9]]


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ## dp from top to bottom
        ## O(n**2), O(1)
        for row in range(1, len(matrix)): #go from the second row to the last row
            for col in range(len(matrix[row])):
                compare =[]
                if col-1>=0:
                    compare.append(matrix[row-1][col-1])
                if col+1<len(matrix[row]):
                    compare.append(matrix[row-1][col+1])
                compare.append(matrix[row-1][col])
                matrix[row][col]+= min(compare)
                
        return min(matrix[-1])