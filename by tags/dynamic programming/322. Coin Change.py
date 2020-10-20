#322. Coin Change

#You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

#You may assume that you have an infinite number of each kind of coin.

 

#Example 1:

#Input: coins = [1,2,5], amount = 11
#Output: 3
#Explanation: 11 = 5 + 5 + 1
#Example 2:

#Input: coins = [2], amount = 3
#Output: -1
#Example 3:

#Input: coins = [1], amount = 0
#Output: 0
#Example 4:

#Input: coins = [1], amount = 1
#Output: 1



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Ben's method
        # if amount==0: return 0
        # dp=[-1]* (amount+1)
        # used= []
        # for i in range(1, amount+1):
        #     if i in coins:
        #         dp[i]=1
        #         used.append(i)
        #     else: 
        #         find_min= float('inf')
        #         for k in used:
        #             if dp[amount-k]!=-1:
        #                 find_min=min(find_min, 1+ dp[amount-k])
        #         if find_min!=float('inf'):
        #             dp[i]=find_min
        #         else:  dp[i]=-1
        # return dp[amount]