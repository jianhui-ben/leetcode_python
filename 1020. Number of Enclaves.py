# 1020. Number of Enclaves
# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
#
# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
#
# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        1, handle boundary. All 0s on the boundary can't form island
        2, dfs on internal area
        O(MN)
        """

        def dfs(mat, r, c):
            mat[r][c] = 0
            for d_r, d_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = d_r + r, d_c + c
                if 0 <= new_r < len(mat) and 0 <= new_c < len(mat[0]) \
                        and mat[new_r][new_c] == 1:
                    dfs(mat, new_r, new_c)

        def dfs2(mat, r, c):
            self.out += 1
            mat[r][c] = 0
            for d_r, d_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = d_r + r, d_c + c
                if 0 <= new_r < len(mat) and 0 <= new_c < len(mat[0]) \
                        and mat[new_r][new_c] == 1:
                    dfs2(mat, new_r, new_c)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r == 0 or r == len(grid) - 1 or c == 0 or c == len(grid[0]) - 1) \
                        and grid[r][c] == 1:
                    dfs(grid, r, c)
        self.out = 0
        for r in range(1, len(grid) - 1):
            for c in range(1, len(grid[0]) - 1):
                if grid[r][c] == 1:
                    dfs2(grid, r, c)

        return self.out