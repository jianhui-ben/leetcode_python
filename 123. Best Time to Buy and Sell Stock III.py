#123. Best Time to Buy and Sell Stock III
#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#Find the maximum profit you can achieve. You may complete at most two transactions.

#Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## dp:
        ## status: hold stock or not (1/0), at most 1 or 2 transactions, days
        ## 1_1, 0_1,1_2, 0_2 
        ## dp[i][1][1] (0)= max(dp[i-1][1][1], -prices[i])
        ## dp[i][0][1] (1) = max(dp[i-1][0][1], dp[i-1][1][1]+prices[i])
        ## dp[i][1][2] (2) = max(dp[i-1][1][2], dp[i-1][0][1]-prices[i])
        ## dp[i][0][2] (3) = max(dp[i-1][0][2], dp[i-1][1][2]+prices[i])
        ## return dp[-1][3]
        
        
        dp = [[0, 0, 0, 0] for _ in range(len(prices))]
        for i in range(len(dp)):
            if i-1==-1:
                dp[i][0], dp[i][2] = -prices[i], -prices[i]
                dp[i][1], dp[i][3] = 0, 0
                continue
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i][0]+prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i][1]-prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i][2]+prices[i])
        return dp[-1][3]
                