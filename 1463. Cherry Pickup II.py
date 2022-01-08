# 1463. Cherry Pickup II
# You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.
#
# You have two robots that can collect cherries for you:
#
# Robot #1 is located at the top-left corner (0, 0), and
# Robot #2 is located at the top-right corner (0, cols - 1).
# Return the maximum number of cherries collection using both robots by following the rules below:
#
# From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
# When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
# When both robots stay in the same cell, only one takes the cherries.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in grid.

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        dp
        stautus: c1, c2, r
        choice: [c1-1: c1+1], [c2-1:c2+1], 9 combos

        """
        mem = {}

        def dp(c1, c2, r):
            if c1 < 0 or c1 >= len(grid[0]) or c2 < 0 or c2 >= len(grid[0]):
                return float('-inf')
            ans = grid[r][c1] + (c1 != c2) * grid[r][c2]
            if r == len(grid) - 1: return ans
            if (c1, c2, r) in mem: return mem[(c1, c2, r)]
            temp = float('-inf')
            for dc1 in [-1, 0, 1]:
                for dc2 in [-1, 0, 1]:
                    new_c1, new_c2 = dc1 + c1, dc2 + c2
                    temp = max(temp, dp(new_c1, new_c2, r + 1))
            mem[(c1, c2, r)] = ans + temp
            return mem[(c1, c2, r)]

        return dp(0, len(grid[0]) - 1, 0)