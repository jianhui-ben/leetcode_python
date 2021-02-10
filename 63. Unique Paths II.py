#63. Unique Paths II
#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

#Now consider if some obstacles are added to the grids. How many unique paths would there be?

#An obstacle and space is marked as 1 and 0 respectively in the grid.
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ##dp
        ## time O(M*N), space O(M*N)
        dp=[[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        ##first row and column:
        for i in range(len(dp)):
            if obstacleGrid[i][0]==1:
                break
            dp[i][0]=1
        
        for i in range(len(dp[0])):
            if obstacleGrid[0][i]==1:
                break
            dp[0][i]=1
        
        for row in range(1, len(obstacleGrid)):
            for col in range(1, len(obstacleGrid[0])):
                if obstacleGrid[row][col]==1:
                    dp[row][col]==0
                else:
                    dp[row][col]= dp[row-1][col]+dp[row][col-1]
        return dp[-1][-1]
