#256. Paint House
#There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

#The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

#For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
#Return the minimum cost to paint all houses.
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        assuming we have two houses
        17      16
        2       16
        17      5
        
        18  
        33
        7
        O(len(costs)), O(1)
        """
        if not costs: return None
        dp = costs[0]
        
        for cost in costs[1:]:
            temp = [None] * 3
            temp[0] = min(dp[1], dp[2]) + cost[0]
            temp[1] = min(dp[0], dp[2]) + cost[1]
            temp[2] = min(dp[0], dp[1]) + cost[2]
            dp = temp
            
        return min(dp)
            
        