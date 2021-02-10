#96. Unique Binary Search Trees

#Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.


class Solution:
    def numTrees(self, n: int) -> int:
        ## dynamic programming:
        ## F(n)= sum(F(i-1) * F(n-i)) for i from 1 to n
        
        dp= [0]*(n+1)
        dp[0], dp[1]=1, 1
        for i in range(2, n+1):
            for k in range(1, i+1):
                dp[i]+= dp[k-1]* dp[i-k]
        return dp[n]
        