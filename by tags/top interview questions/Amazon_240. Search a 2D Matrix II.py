#240. Search a 2D Matrix II
#Write an efficient algorithm that searches for a target value in an m x n integer matrix. 
#The matrix has the following properties:

#Integers in each row are sorted in ascending from left to right.
#Integers in each column are sorted in ascending from top to bottom.
 

#Example 1:


#Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
#Output: true
class Solution:
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## a very smart method:
        r, c=len(matrix)-1, len(matrix[0])-1
        s_r, s_c= r, 0
        while s_r>=0 and s_c<=c:
            if matrix[s_r][s_c]== target:
                return True
            elif matrix[s_r][s_c]> target:
                s_r-=1
            else:
                s_c+=1
        return False
        
        
#         ### method 2: Ben's method
#     def crop_search(self, matrix, up, down, left, right, target):
#         if up>down or left>right: return False
#         elif target<matrix[up][left] or target> matrix[down][right]:
#             return False
#         elif target==matrix[up][left] or target==matrix[down][right]:
#             return True
#         change=0
#         while up<=down and matrix[up][right]<target:
#             up+=1
#             change+=1
#         while down>=up and matrix[down][left]>target:
#             down-=1
#             change+=1
        
#         while left<=right and matrix[down][left]<target:
#             left+=1
#             change+=1

#         while right>=left and matrix[up][right]<target:
#             right-=1
#             change+=1
#         if change>0:
#             return self.crop_search(matrix, up, down, left, right, target)
#         else:
#             for r in matrix[up: down+1]:
#                 for c in r[left:right+1]:
#                     if c==target: return True
#             return False
                
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if not matrix: return False
#         r, c=len(matrix), len(matrix[0])
#         return self.crop_search(matrix, 0, r-1, 0, c-1, target)
        
        