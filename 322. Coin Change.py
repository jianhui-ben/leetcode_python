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
        ## naive O(# of coins * amount^# of coins)
        if amount<0: return -1
        if amount ==0: return 0
        out= float('inf')
        
        for coin in coins:
            subproblem = self.coinChange(coins, amount- coin)
            if subproblem==-1: continue
            out=min(out, subproblem+1)
        return out if out!=float('inf') else -1
    

    
        ## improve it with mem top down recursion method
        ## the num of subproblems was reduce to O(n) so total time O(# of coins * n)
        
        mem = dict()
        def dp(amount):
            if amount in mem: return mem[amount]
            if amount<0: return -1
            if amount ==0: return 0
            out= float('inf')
            for coin in coins:
                subproblem = dp(amount- coin)
                if subproblem==-1: continue
                out=min(out, subproblem+1)
            mem[amount] = out if out!=float('inf') else -1
            return mem[amount]
        return dp(amount)
    
    
        ## improve it with bottom up iteration method:
        ## similar to top down recursion, time O(k*n)
        dp =  [float('inf')] * (amount+1)
        dp[0]=0
        for i in range(1, amount+1):
            for coin in coins:
                if i-coin<0: continue
                dp[i]=min(dp[i], 1+dp[i-coin])    
        return dp[-1] if dp[-1]!=float('inf') else -1
        
        