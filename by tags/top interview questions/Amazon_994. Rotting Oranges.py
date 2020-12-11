#994. Rotting Oranges

#In a given grid, each cell can have one of three values:

#the value 0 representing an empty cell;
#the value 1 representing a fresh orange;
#the value 2 representing a rotten orange.
#Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

#Return the minimum number of minutes that must elapse until no cell has a fresh orange.  
#If this is impossible, return -1 instead.


#Input: [[2,1,1],[1,1,0],[0,1,1]]
#Output: 4


class Solution:
    def change(self, queue, grid):
        new_queue=[]
        while queue:
            row, col= queue.pop()
            if row-1>=0 and grid[row-1][col]==1:
                grid[row-1][col]=2
                new_queue.append((row-1, col))
            if row+1<len(grid) and grid[row+1][col]==1:
                grid[row+1][col]=2
                new_queue.append((row+1, col))
            if col-1>=0 and grid[row][col-1]==1:
                grid[row][col-1]=2
                new_queue.append((row, col-1))
            if col+1< len(grid[row]) and grid[row][col+1]==1:
                grid[row][col+1]=2
                new_queue.append((row, col+1))
            
        return new_queue, grid
    ## time  O(m*n), space O(m *n)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue= []
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] ==2:
                    queue.append((row, col))
                    
        self.out=0
        while queue:
            queue, grid=self.change(queue, grid)
            self.out+=1
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] ==1:
                    return -1
        return max(self.out-1, 0)