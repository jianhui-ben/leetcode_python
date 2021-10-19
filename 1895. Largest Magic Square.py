# 1895. Largest Magic Square
# A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.
#
# Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.
#
#
# Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
# Output: 3
# Explanation: The largest magic square has a size of 3.
# Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
# - Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
# - Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
# - Diagonal sums: 5+4+3 = 6+4+2 = 12


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:

        """
        prefix sum + brute force
        find ways to represent rowsum, colsum, major/minor diagonal sum
        """
        m, n = len(grid), len(grid[0])
        dp = [[[0, 0, 0, 0] for _ in range(n + 1)] for _ in range(m + 1)]

        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                dp[row][col][0] = dp[row][col - 1][0] + grid[row - 1][col - 1]
                dp[row][col][1] = dp[row - 1][col][1] + grid[row - 1][col - 1]
                dp[row][col][2] = dp[row - 1][col - 1][2] + grid[row - 1][col - 1]
                dp[row][col][3] = dp[row - 1][col + 1][3] + grid[row - 1][col - 1] if col < n else grid[row - 1][
                    col - 1]

        for win in range(min(m, n), 0, -1):
            for row in range(win, len(dp)):
                for col in range(win, len(dp[0])):
                    val = dp[row][col][2] - dp[row - win][col - win][2]

                    if col + 1 < len(dp[0]):
                        if val != dp[row][col - win + 1][3] - dp[row - win][col + 1][3]:
                            continue
                    else:
                        if val != dp[row][col - win + 1][3]:
                            continue

                    if any(dp[r][col][0] - dp[r][col - win][0] != val for r in range(row, row - win, -1)):
                        continue
                    if any(dp[row][c][1] - dp[row - win][c][1] != val for c in range(col, col - win, -1)):
                        continue

                    return win
        return 1


