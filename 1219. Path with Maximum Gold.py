#1219. Path with Maximum Gold
#In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

#Return the maximum amount of gold you can collect under the conditions:

#Every time you are located in a cell you will collect all the gold in that cell.
#From your position you can walk one step to the left, right, up or down.
#You can't visit the same cell more than once.
#Never visit a cell with 0 gold.
#You can start and stop collecting gold from any position in the grid that has some gold.
 

#Example 1:

#Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
#Output: 24
#Explanation:
#[[0,6,0],
# [5,8,7],
# [0,9,0]]
#Path to get the maximum gold, 9 -> 8 -> 7.

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        ## dfs backtracking
        ## time O(R**2 * C **2)
        out = 0
        
        def backtrack(grid, r, c, cur):
            nonlocal out
            if r>=0 and c>=0 and r<len(grid) and c<len(grid[0]) and grid[r][c]!=0:
                v= grid[r][c]
                out=max(out, cur+v)
                grid[r][c]=0
                backtrack(grid, r+1, c, cur+v)
                backtrack(grid, r-1, c, cur+v)
                backtrack(grid, r, c+1, cur+v)
                backtrack(grid, r, c-1, cur+v)
                grid[r][c]=v
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]!=0:
                    backtrack(grid, r, c, 0)
        return out
        