#54. Spiral Matrix
#Given an m x n matrix, return all elements of the matrix in spiral order.

 

#Example 1:
#1 2 3
#4 5 6 
#7 8 9 

#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [1,2,3,6,9,8,7,4,5]
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        rowBegin, columnBegin= 0, 0
        rowEnd, columnEnd= len(matrix), len(matrix[0])
        ans=[]
        while columnEnd> columnBegin and rowEnd>rowBegin:
            for i in range(columnBegin, columnEnd):
                ans.append(matrix[rowBegin][i])
            
            for j in range(rowBegin+1, rowEnd):
                ans.append(matrix[j][columnEnd-1])
            
            if rowEnd!= rowBegin+1:
                for i in range(columnEnd-2, columnBegin-1, -1):
                    ans.append(matrix[rowEnd-1][i])
            if columnEnd!= columnBegin+1:
                for j in range(rowEnd-2, rowBegin, -1):
                    ans.append(matrix[j][columnBegin])
            rowBegin+=1
            columnBegin+=1
            rowEnd-=1
            columnEnd-=1
            # print(ans)
        return ans