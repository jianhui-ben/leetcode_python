#1428. Leftmost Column with at Least a One
#(This problem is an interactive problem.)

#A row-sorted binary matrix means that all elements are 0 or 1 and each row of the matrix is sorted in non-decreasing order.

#Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of the leftmost column with a 1 in it. If such an index does not exist, return -1.

#You can't access the Binary Matrix directly. You may only access the matrix using a BinaryMatrix interface:

#BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
#BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2 elements [rows, cols], which means the matrix is rows x cols.
#Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

#For custom testing purposes, the input will be the entire binary matrix mat. You will not have access to the binary matrix directly.

 

#Example 1:



#Input: mat = [[0,0],[1,1]]
#Output: 0
#Example 2:



#Input: mat = [[0,0],[0,1]]
#Output: 1
#Example 3:



#Input: mat = [[0,0],[0,0]]
#Output: -1
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """
        approach 2:
        greedy: start from top right to bootom left
        time: N+M, space O(1)
        """
        row, col = binaryMatrix.dimensions()
        
        cur_r, cur_c, found = 0, col - 1, False
        while cur_r < row:
            
            while cur_c >= 0 and binaryMatrix.get(cur_r, cur_c):
                found = True
                cur_c -= 1
            cur_r += 1
        return cur_c + 1 if found else -1
            
        
        
        
        
#         """
#         approach 1: binary search
#         -get row and col, initialize the leftmost = col
#         - for each row, we check matrix[row][leftmost] == 1
#            - if yes, perform binary search on this row to update the leftmost
#            - binary serarch to find the first 1
#         time: nlogn ~ 600
        
#         """
#         def binary_search(binaryMatrix, r, left, right):
            
#             ans = right
#             while left <= right:
#                 mid = left + (right - left) // 2
#                 if binaryMatrix.get(r, mid):
#                     ans = mid
#                     right = mid - 1
#                 else:
#                     left = mid + 1
            
#             return ans
                    
        
#         row, col = binaryMatrix.dimensions()
        
#         leftmost, found = col - 1, False
#         for r in range(row):
#             if binaryMatrix.get(r, leftmost):
#                 found = True
#                 leftmost = binary_search(binaryMatrix, r, 0, leftmost)
        
#         return leftmost if found else -1
            
            
            
        
        
        