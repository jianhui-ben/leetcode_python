# 1937. Maximum Number of Points with Cost
#
# You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.
#
# To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.
#
# However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.
#
# Return the maximum number of points you can achieve.
#
# abs(x) is defined as:
#
# x for x >= 0.
# -x for x < 0.

from collections import deque


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        update


        previous dp:
        1, 3, 5, 3, 4

        left:
        1, 3, 5, 4, 4


        right:
        3  4  5  3  4

        3. 4. 5. 4. 4

        next line:
        2, 6, 3, 2, 1
        ^
        """

        dp = [k for k in points[0]]

        for row in range(1, len(points)):

            left = [dp[0]]
            for i in range(1, len(dp)):
                left.append(max(left[-1] - 1, dp[i]))

            right = deque([dp[-1]])
            for i in range(len(dp) - 2, -1, -1):
                right.appendleft(max(right[0] - 1, dp[i]))

            for i in range(len(dp)):
                dp[i] = max(left[i], right[i]) + points[row][i]
        return max(dp)