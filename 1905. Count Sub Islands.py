# 1905. Count Sub Islands
# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.
#
# An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.
#
# Return the number of islands in grid2 that are considered sub-islands.


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        1, need to store all the islands in term of lists for both grids
        2, union find + dfs
        3, compare it
        """
        row, col, cur_island = len(grid1), len(grid1[0]), []

        def dfs(grid, r, c):
            nonlocal cur_island, row, col
            grid[r][c] = 0
            cur_island.append(r * col + c)
            for d_r, d_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = d_r + r, d_c + c
                if 0 <= new_r < row and 0 <= new_c < col and grid[new_r][new_c] == 1:
                    dfs(grid, new_r, new_c)

        def get_islands(grid):
            nonlocal cur_island
            out = []
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 1:
                        cur_island = []
                        dfs(grid, r, c)
                        out.append(list(cur_island))
            return out

        l_islands2 = get_islands(grid2)
        out = len(l_islands2)
        for island in l_islands2:
            for n in island:
                r, c = n // col, n % col
                # print(n, r, c, row, col)
                if grid1[r][c] == 0:
                    out -= 1
                    break
        return out






