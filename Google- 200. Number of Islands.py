#200. Number of Islands
#Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

#An island is surrounded by water and is formed by connecting adjacent lands horizontally
#or vertically. You may assume all four edges of the grid are all surrounded by water.

 

#Example 1:

#Input: grid = [
#  ["1","1","1","1","0"],
#  ["1","1","0","1","0"],
#  ["1","1","0","0","0"],
#  ["0","0","0","0","0"]
#]
#Output: 1
#Example 2:

#Input: grid = [
#  ["1","1","0","0","0"],
#  ["1","1","0","0","0"],
#  ["0","0","1","0","0"],
#  ["0","0","0","1","1"]
#]
#Output: 3


##graph theory

class Solution:
    def dfs(self, grid, i, j):
        if i>=0 and i<=len(grid)-1 and j>=0 and j<=len(grid[i])-1 \
        and grid[i][j]=='1':
        
            grid[i][j]=0
            self.dfs(grid, i-1, j)
            self.dfs(grid, i+1, j)
            self.dfs(grid, i, j-1)
            self.dfs(grid, i, j+1)
            return 1
        
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid)==0:
            return 0
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    ans+= self.dfs(grid, i, j)
        
        return ans
    