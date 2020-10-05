#48. Rotate Image (https://leetcode.com/problems/rotate-image/)

#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
#DO NOT allocate another 2D matrix and do the rotation.

 

#Example 1:


#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [[7,4,1],[8,5,2],[9,6,3]]


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for x in range(len(matrix)):
            for y in range(x, len(matrix[0])):
                if x!=y:
                    temp= matrix[x][y]
                    matrix[x][y]= matrix[y][x]
                    matrix[y][x]=temp
        for x in range(len(matrix)):
            head, tail=0, len(matrix[0])-1
            while head<tail:
                temp=matrix[x][head]
                matrix[x][head]=matrix[x][tail]
                matrix[x][tail]=temp
                head+=1
                tail-=1
        
                