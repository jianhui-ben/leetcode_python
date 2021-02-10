#256. Paint House
#There are a row of n houses, each house can be painted with one of the 
#three colors: red, blue or green. The cost of painting each house with 
#a certain color is different. You have to paint all the houses such that 
#no two adjacent houses havethe same color, and you need to cost the least. Return the minimum cost.

#The cost of painting each house with a certain color is represented by 
#a n x 3 cost matrix. For example, costs[0][0] is the cost of painting 
#house 0 with color red; costs[1][2] is the cost of painting house 1 with 
#color green, and so on... Find the minimum cost to paint all houses.

#Example 1:

#Input: [[14,2,11],[11,14,5],[14,3,10]]
#Output: 10
#Explanation: Paint house 0 into blue, paint house 1 into green,
#paint house 2 into blue. Minimum cost: 2 + 5 + 3 = 10.
#Example 2:

#Input: [[1,2,3],[1,4,6]]
#Output: 3


class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        if not costs: return 0
        
        ##traversing
        for i in range(1, len(costs)):
            costs[i][0]+=min(costs[i-1][1],costs[i-1][2])
            costs[i][1]+=min(costs[i-1][0],costs[i-1][2])
            costs[i][2]+=min(costs[i-1][0],costs[i-1][1])
            
        return min(costs[-1])
                