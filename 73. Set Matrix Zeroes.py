#73. Set Matrix Zeroes
#Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

#Follow up:

#A straight forward solution using O(mn) space is probably a bad idea.
#A simple improvement uses O(m + n) space, but still not the best solution.
#Could you devise a constant space solution?

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ##brute force: space(n+m)
        m, n= [False] * len(matrix), [False]*len(matrix[0])
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==0:
                    m[r], n[c]=True, True
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if m[r] or n[c]:
                    matrix[r][c]=0
        return