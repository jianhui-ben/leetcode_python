#312. Burst Balloons
#You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

#If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

#Return the maximum coins you can collect by bursting the balloons wisely.

 

#Example 1:

#Input: nums = [3,1,5,8]
#Output: 167
#Explanation:
#nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
#coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        ## dp 
        ## dp[i][j]=m: max coin is x for nums[i+1:j]
        ## where 0<=i<=len(nums)+1 and j>i
        ## return dp[1][len(nums)]
        ## backward traverse:
        ## if j<=i: continue
        ## if j-i==1: return 0
        ## dp[i][j]=dp[i][k]+dp[k][j]+ points[i]*points[k]*points[j]
        ## O(N**2)
        ## add a left and right boundary around nums
        points = [1]+nums+[1]
        dp = [[0 for _ in range(len(points))] for _ in range(len(points))]
        for i in range(len(dp)-1, -1, -1):
            for j in range(i+1, len(dp[0])):
                if j-i<1: continue
                for k in range(i+1, j, 1):
                    dp[i][j]= max(dp[i][j], dp[i][k]+dp[k][j]+ points[i]*points[k]*points[j])
        
        return dp[0][-1]
        