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

def coinChange(coins, amount):    
    #Ben's method
    if amount==0: return 0
    dp=[float('inf')]* (amount+1)
    used= []
    for i in range(1, amount+1):
        if i in coins:
            dp[i]=1
            used.append(i)
        else: 
            for k in used:
                dp[i]= min(dp[i],1+dp[i-k])

    return dp[-1] if dp[-1]<float('inf') else -1

coins= [1,2,5]
amount=11
coinChange(coins, amount)


min(float('inf'),1+float('inf'))