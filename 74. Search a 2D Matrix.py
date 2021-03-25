#74. Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## time O(n), space O(1)
        r, c = len(matrix), len(matrix[0])
        i_r, i_c= r-1, 0
        
        while i_r>=0 and i_c<c:
            if matrix[i_r][i_c]==target:
                return True
            elif matrix[i_r][i_c]>target:
                i_r-=1
            else:
                i_c+=1
        
        return False
