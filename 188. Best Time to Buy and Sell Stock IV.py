#188. Best Time to Buy and Sell Stock IV
#You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

#Find the maximum profit you can achieve. You may complete at most k transactions.

#Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

#Example 1:

#Input: k = 2, prices = [2,4,1]
#Output: 2
#Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        ##dp
        ##status: currently if we have stocks, max steps allowed, current index on prices
        ## choice: wait or do action
        ## dp[0][k][i]= profit
        ## return dp[0][k][n-1]
        
        ## dp[0][k][i] = max(dp[0][k][i-1], dp[1][k][i-1]+prices[i])
        ## dp[1][k][i] = max(dp[1][k][i-1], dp[0][k-1][i-1]-prices[i])
        ## base case:
        ## dp[0][1][i]= max(dp[0][1][i-1], dp[1][1][i-1]+prices[i])
        ## dp[1][1][i]= max(dp[1][1][i-1], dp[0][0][i-1]-prices[i])
        ##            = max(dp[1][1][i-1], -prices[i])
        
        
        ## 2d array dp[i][1 or 0 / hold or not]
        if not prices or not k: return 0
        dp = [[[0, 0] for _ in range(k+1)] for _ in range(len(prices))]
        
        for i in range(len(dp)):
            for k in range(len(dp[i])):
                if i-1==-1:
                    dp[i][k][0]= 0
                    dp[i][k][1]=-prices[i]
                    continue
                elif k==0:
                    dp[i][k][0]= 0
                    dp[i][k][1] = float('-inf')
                    continue
            
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+ prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
        return dp[-1][-1][0]
        
