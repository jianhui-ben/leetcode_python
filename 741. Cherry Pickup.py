# 741. Cherry Pickup
# You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.
#
# 0 means the cell is empty, so you can pass through,
# 1 means the cell contains a cherry that you can pick up and pass through, or
# -1 means the cell contains a thorn that blocks your way.
# Return the maximum number of cherries you can collect by following the rules below:
#
# Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
# After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
# When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
# If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        dp
        r1, c1, r2 can determine two persons' location.
        dp() return the max cherries from (r1, c1), (r2, c2)
        """
        mem, n = {}, len(grid)

        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2
            if r1 == n or r2 == n or c1 == n or c2 == n \
                    or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            if r1 == c1 == n - 1:
                return grid[r1][c1]
            if (r1, c1, r2) in mem:
                return mem[(r1, c1, r2)]
            ans = grid[r1][c1] + (r1 != r2) * grid[r2][c2]
            ans += max(dp(r1 + 1, c1, r2), dp(r1, c1 + 1, r2), dp(r1 + 1, c1, r2 + 1), dp(r1, c1 + 1, r2 + 1))
            mem[(r1, c1, r2)] = ans
            return mem[(r1, c1, r2)]

        return max(0, dp(0, 0, 0))


