#518. Coin Change 2
#You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

#Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

#You may assume that you have an infinite number of each kind of coin.

#The answer is guaranteed to fit into a signed 32-bit integer.

 

#Example 1:

#Input: amount = 5, coins = [1,2,5]
#Output: 4
#Explanation: there are four ways to make up the amount:
#5=5
#5=2+2+1
#5=2+1+1+1
#5=1+1+1+1+1


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ## status: the coin selection and the amount we are trying to reach
        ## choice: choose or not
        ## dp[i][j]= x: there're x ways to get i by selecting coins[:j]
        ## where 0<=i<=amount, 0<=j<=len(coins)
        ## return dp[-1][-1]
        ## status change: if not choose coin[j-1], dp[i][j-1]
        ## if choose coin[j-1], then dp[i-coin[j-1]][j]
        
        ## typical DP O(len(coin) * amount)
        dp= [[0 for _ in range(len(coins)+1)] for _ in range(amount+1)]
        options = set(coins)
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i==0:
                    dp[i][j]=1
                elif j==0:
                    continue
                elif i>=coins[j-1]:
                    dp[i][j] = dp[i][j-1]+dp[i-coins[j-1]][j]
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[-1][-1]