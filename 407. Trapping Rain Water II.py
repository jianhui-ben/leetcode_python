#407. Trapping Rain Water II
#Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ## BFS + heap
        ## very interesting problem
        
        res = 0
        import heapq
        queue = []
        visited = [[0 for _ in range(len(heightMap[0]))] for _ in range(len(heightMap))]
        
        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                if i==0 or j==0 or i==len(heightMap)-1 or j ==len(heightMap[0])-1:
                    heapq.heappush(queue, (heightMap[i][j],i, j))
                    visited[i][j] = 1
                
        while queue:
            low, i, j = heapq.heappop(queue)
            
            for a,b in [(0, 1), (0, -1), (1,0), (-1, 0)]:
                new_i, new_j = i+a, j+b
                if 0<=new_i<len(heightMap) and 0<=new_j<len(heightMap[0]) and visited[new_i][new_j]==0:
                    if heightMap[new_i][new_j]<low:
                        res+= low-heightMap[new_i][new_j]
                        
                    heapq.heappush(queue, (max(heightMap[new_i][new_j], low),new_i, new_j))    
                    visited[new_i][new_j]=1
        return res
                        