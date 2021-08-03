#827. Making A Large Island
#You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

#Return the size of the largest island in grid after applying this operation.

#An island is a 4-directionally connected group of 1s.

 

#Example 1:

#Input: grid = [[1,0],[0,1]]
#Output: 3
#Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
#Example 2:

#Input: grid = [[1,1],[1,0]]
#Output: 4
#Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
#Example 3:

#Input: grid = [[1,1],[1,1]]
#Output: 4
#Explanation: Can't change any 0 to 1, only one island with area = 4.
class Solution:

    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        label every single cell (1) to correponding island
        check if any 0s conconect two separate islands
        O(m*n); O(m*n)
        """
        
        island_map = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        island_area = defaultdict(int)
        island_idx = 1
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        
        def dfs(row, col, island_idx):
            nonlocal island_map, island_area, d
            island_map[row][col] = island_idx
            island_area[island_idx] += 1
            
            for d_r, d_c in d:
                new_r, new_c = row + d_r, col + d_c
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0])\
                and grid[new_r][new_c] == 1 and island_map[new_r][new_c] == -1 :
                    dfs(new_r, new_c, island_idx)
            

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and island_map[row][col] == -1:
                    dfs(row, col, island_idx)
                    island_idx += 1
                    
        
        out = max(island_area.values()) if island_area else 1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if island_map[row][col] == -1:
                    connected_island = set()
                    for d_r, d_c in d:
                        new_r, new_c = row + d_r, col + d_c
                        if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]) \
                        and island_map[new_r][new_c] != -1 \
                        and island_map[new_r][new_c] not in connected_island:
                            connected_island.add(island_map[new_r][new_c])
                            
                    # print(row, col, connected_island)
                    cur_area = 1
                    for island in connected_island:
                        cur_area += island_area[island]
                    out = max(out, cur_area)
                    
        return out
                        