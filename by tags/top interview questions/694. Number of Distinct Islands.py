#694. Number of Distinct Islands
#Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

#Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

#Example 1:
#11000
#11000
#00011
#00011
#Given the above grid map, return 1.

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ##dfs and hash table
        
        self.count=0
        self.islands=set()
        
        def dfs(grid, r,c, cur_island):
            if r>=0 and r<len(grid) and c>=0 and c<len(grid[0]) and grid[r][c]==1:
                cur_island.append((r,c))
                grid[r][c]=0
                cur_island=dfs(grid, r+1,c, cur_island)
                cur_island=dfs(grid, r-1,c, cur_island)
                cur_island=dfs(grid, r,c+1, cur_island)
                cur_island=dfs(grid, r,c-1, cur_island)
            return cur_island

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    current_island=dfs(grid, r, c, [])
                    ## convert coordinates
                    current_island.sort()
                    r0, c0= current_island[0]
                    current_island='*'.join([str(r_i-r0)+'-' +str(c_i-c0) for r_i, c_i in current_island])
                    if current_island not in self.islands:
                        self.count+=1
                        self.islands.add(current_island)
        return self.count