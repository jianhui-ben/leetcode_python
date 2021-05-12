#309. Best Time to Buy and Sell Stock with Cooldown
#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

#After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
#Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## dp
        ## status: hold or not (1/0), days
        ## dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
        ## dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        ## base case: dp[0][1] = -prices[i], dp[0][0] = 0, 
        ##            dp[1][1]= max(dp[i-1][1],-prices[i])
        
        dp = [[0, 0] for _ in range(len(prices))]
        for i in range(len(dp)):
            if i==0:
                dp[i][1], dp[i][0] = -prices[i], 0
            elif i==1:
                dp[i][1], dp[i][0] = max(dp[i-1][1],-prices[i]), \
                                    max(dp[i-1][0], dp[i-1][1]+prices[i])
            else:
                dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        return dp[-1][0]
 
