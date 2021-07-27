#1765. Map of Highest Peak
#You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

#If isWater[i][j] == 0, cell (i, j) is a land cell.
#If isWater[i][j] == 1, cell (i, j) is a water cell.
#You must assign each cell a height in a way that follows these rules:

#The height of each cell must be non-negative.
#If the cell is a water cell, its height must be 0.
#Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
#Find an assignment of heights such that the maximum height in the matrix is maximized.

#Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        """BFS
        
         1  1  X
         X  1  1
         1  2  2
         
         
        
        
        """
        
        out = [[None for _ in isWater[0]] for _ in isWater]
        
        queue = []
        
        for row in range(len(isWater)):
            for col in range(len(isWater[0])):
                if isWater[row][col]:
                    queue.append((row, col))
                    out[row][col] = 0
        height = 0
        while queue:            
            temp_queue = []
            
            d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            for row, col in queue:
                                
                for d_row, d_col in d:
                    new_row, new_col = row + d_row, col + d_col
                    
                    if 0 <= new_row < len(isWater) and 0 <= new_col < len(isWater[0]) \
                    and out[new_row][new_col] == None:
                        out[new_row][new_col] = height + 1
                        temp_queue.append((new_row, new_col))
            
            height += 1
            queue = temp_queue
            
        return out
                        
 
