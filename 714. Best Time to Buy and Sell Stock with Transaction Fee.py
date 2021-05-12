#714. Best Time to Buy and Sell Stock with Transaction Fee
#You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

#Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

#Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

#Example 1:

#Input: prices = [1,3,2,8,4,9], fee = 2
#Output: 8
#Explanation: The maximum profit can be achieved by:
#- Buying at prices[0] = 1
#- Selling at prices[3] = 8
#- Buying at prices[4] = 4
#- Selling at prices[5] = 9
#The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        ## dp
        ## status: hold or not (1/0), days
        ## dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i]-fee)
        ## dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        ## base case: dp[0][1] = -prices[i]-fee, dp[0][0] = 0, 
        
        dp = [[0, 0] for _ in range(len(prices))]
        for i in range(len(dp)):
            if i==0:
                dp[i][1], dp[i][0] = -prices[i]-fee, 0
            else:
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i]-fee)
                dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        return dp[-1][0]