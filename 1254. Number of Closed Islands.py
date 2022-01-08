# 1254. Number of Closed Islands
#
# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
#
# Return the number of closed islands.

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        1, handle boundary. All 0s on the boundary can't form island
        2, dfs on internal area
        O(MN)
        """

        def dfs(mat, r, c):
            mat[r][c] = 1
            for d_r, d_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = d_r + r, d_c + c
                if 0 <= new_r < len(mat) and 0 <= new_c < len(mat[0]) \
                        and mat[new_r][new_c] == 0:
                    dfs(mat, new_r, new_c)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r == 0 or r == len(grid) - 1 or c == 0 or c == len(grid[0]) - 1) \
                        and grid[r][c] == 0:
                    grid[r][c] = 1
                    dfs(grid, r, c)
        out = 0
        for r in range(1, len(grid) - 1):
            for c in range(1, len(grid[0]) - 1):
                if grid[r][c] == 0:
                    out += 1
                    dfs(grid, r, c)

        return out


