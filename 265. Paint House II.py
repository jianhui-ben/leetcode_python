#265. Paint House II
#There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

#The cost of painting each house with a certain color is represented by an n x k cost matrix costs.

#For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
#Return the minimum cost to paint all houses.
#Example 1:

#Input: costs = [[1,5,3],[2,9,4]]
#Output: 5
#Explanation:
#Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
#Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.

##min heap


import heapq
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        """
        keep a stack of k
        k[i] = the min cost up to the current house if current house is using color i
        return k
        
        
        for every house i, we also need to track 
        the min cost up to house i - 1, and the color in house i - 1
        the second min cost up to house i - 1, and the color in house i-1
        
        time: O(nklogk)
        space: O(k)
        
        """
        heap = [(c, i)for i, c in enumerate(costs[0])]
        
        heapq.heapify(heap)
        for house_i in range(1, len(costs)):
            
            lowest, second_lowest = heapq.heappop(heap), heapq.heappop(heap)
            
            temp_heap = []
            
            for color_i, cost in enumerate(costs[house_i]):
                
                if color_i != lowest[1]:
                    heapq.heappush(temp_heap, (lowest[0] + cost, color_i))
                else:
                    heapq.heappush(temp_heap, (second_lowest[0] + cost, color_i))
            heap = temp_heap
        return heapq.heappop(heap)[0]
            
            
            
            
        
            
            
            

        