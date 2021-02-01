#695. Max Area of Island
#Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

#Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

#Example 1:

#[[0,0,1,0,0,0,0,1,0,0,0,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,1,1,0,1,0,0,0,0,0,0,0,0],
# [0,1,0,0,1,1,0,0,1,0,1,0,0],
# [0,1,0,0,1,1,0,0,1,1,1,0,0],
# [0,0,0,0,0,0,0,0,0,0,1,0,0],
# [0,0,0,0,0,0,0,1,1,1,0,0,0],
# [0,0,0,0,0,0,0,1,1,0,0,0,0]]
#Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
#Example 2:

#[[0,0,0,0,0,0,0,0]]


class Solution:
    def dfs(self, grid, i, j, cur_area):
        if i>=0 and i<=len(grid)-1 and j>=0 and j<=len(grid[i])-1 \
        and grid[i][j]==1:
        
            grid[i][j]=0
            cur_area+=1
            cur_area=self.dfs(grid, i-1, j, cur_area)
            cur_area=self.dfs(grid, i+1, j, cur_area)
            cur_area=self.dfs(grid, i, j-1, cur_area)
            cur_area=self.dfs(grid, i, j+1, cur_area)
        return cur_area
        
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or len(grid)==0:
            return 0
        ans=0    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    ans= max(ans, self.dfs(grid, i, j, 0))
        return ans   
        