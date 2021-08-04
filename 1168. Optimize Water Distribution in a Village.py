#1168. Optimize Water Distribution in a Village
#There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

#For each house i, we can either build a well inside it directly with cost wells[i - 1] (note the -1 due to 0-indexing), or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes, where each pipes[j] = [house1j, house2j, costj] represents the cost to connect house1j and house2j together using a pipe. Connections are bidirectional.

#Return the minimum total cost to supply water to all houses.

 

#Example 1:



#Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
#Output: 3
#Explanation: 
#The image shows the costs of connecting houses using pipes.
#The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        
        """
        minimal spanning tree
        prim's algorithm
        time: E + V + V + E * log E -- > O(E log E)
        space: E + V
        """
        
        stored = defaultdict(list)
        for house_i, house_j, cost in pipes:
            stored[house_i].append((cost, house_j))
            stored[house_j].append((cost, house_i))
        
        for i, cost in enumerate(wells, 1):
            stored[i].append((cost, 0))
            stored[0].append((cost, i))
            
        heapq.heapify(stored[0])
        minheap = stored[0]
        visited = set([0])
        out = 0
        
        while minheap and len(visited) < n + 1:
            
            cost, cur_house = heapq.heappop(minheap)
            if cur_house not in visited:
                visited.add(cur_house)
                out += cost
                
                for next_cost, next_house in stored[cur_house]:
                    heapq.heappush(minheap, (next_cost, next_house))
        return out
                    
                
                