#877. Stone Game
#Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

#The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

#Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

#Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

 class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        ## dp
        ## if first person selects nums[i], then it can get nums[i]+ dp[i+1][j].sec
        ## and the second person will get dp[i+1][j].first
        ## 博弈类问题 O(N2)
        dp =  [[(None, None) for _ in range(len(piles))] for _ in range(len(piles))]
        for i in range(len(dp)-1, -1, -1):
            for j in range(len(dp[i])):
                if j<i:
                    continue
                elif j==i:
                    dp[i][j] = (piles[i], 0)
                else:
                    if piles[i]+ dp[i+1][j][1]>= piles[j]+dp[i][j-1][1]:
                        dp[i][j]= (piles[i]+ dp[i+1][j][1],dp[i+1][j][0])
                    else:
                        dp[i][j] = (piles[j]+dp[i][j-1][1], dp[i][j-1][0])
            
        return dp[0][-1][0]>dp[0][-1][1]
        
        
