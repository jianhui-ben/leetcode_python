#276. Paint Fence
#You are painting a fence of n posts with k different colors. You must paint the posts following these rules:

#Every post must be painted exactly one color.
#There cannot be three or more consecutive posts with the same color.
#Given the two integers n and k, return the number of ways you can paint the fence.

 

#Example 1:


#Input: n = 3, k = 2
#Output: 6
#Explanation: All the possibilities are shown.
#Note that painting all the posts red or all the posts green is invalid because there cannot be three posts in a row with the same color.

class Solution:
    def numWays(self, n: int, k: int) -> int:
        """
        n:3, k:3
        very interesting problem, check out the leetcode solution
        dp:
        dp[n] = # of possible combos
        dp[n] = dp[n-1] * (k - 1) - dp[n - 2] * (k - 1)
        """
        if k == 1 and n > 2: return 0
        if n == 1: return k
        if n == 2: return k * k
        first, second = k, k * k
        for i in range(3, n + 1):
            temp = second
            second = (k - 1) * second + (k - 1) * first
            first = temp
            
        return second
