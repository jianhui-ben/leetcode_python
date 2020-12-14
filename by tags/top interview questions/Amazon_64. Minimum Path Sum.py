#64. Minimum Path Sum

#Given a m x n grid filled with non-negative numbers, find a path from
#top left to bottom right, which minimizes the sum of all numbers along its path.

#Note: You can only move either down or right at any point in time.

 

#Example 1:


#Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
#Output: 7
#Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.



class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ##dp:
        out_grid= grid.copy()
        if not grid: return None
        for i in range(1, len(grid[0])):
            out_grid[0][i]= grid[0][i-1]+ grid[0][i]
        for i in range(1, len(grid)):
            out_grid[i][0]= grid[i-1][0]+ grid[i][0]
        for r in range(1, len(out_grid)):
            for c in range(1, len(out_grid[0])):
                out_grid[r][c]= grid[r][c]+min(out_grid[r-1][c],out_grid[r][c-1])
        return out_grid[-1][-1]          
        
        
        
        
        
        
        ##dfs to find all paths and find max
        ## 2**N time, O(1) space
        self.min=float('inf') 
        if not grid: return None
        def dfs(grid, r, c, cur_sum):
            if r==len(grid)-1 and c==len(grid[0])-1:
                self.min=min(self.min, cur_sum)
            else:
                if r<len(grid)-1 and cur_sum<self.min:
                    dfs(grid, r+1, c, cur_sum+ grid[r+1][c])
                if c<len(grid[0])-1 and cur_sum<self.min:
                    dfs(grid, r, c+1, cur_sum+ grid[r][c+1])  
        dfs(grid, 0,0, grid[0][0])
        return self.min
        
        
        
