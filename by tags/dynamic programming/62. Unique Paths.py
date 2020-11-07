#62. Unique Paths (https://leetcode.com/problems/unique-paths/)

#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

#The robot can only move either down or right at any point in time. The robot is trying to 
#reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

#How many possible unique paths are there?

##time O(m*n), space o(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * (n) for _ in range(m)]
        for i in range(1, m):
            for k in range(1, n):
                dp[i][k]=dp[i][k-1]+dp[i-1][k]
        return dp[-1][-1]