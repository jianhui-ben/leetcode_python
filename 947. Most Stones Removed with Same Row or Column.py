#947. Most Stones Removed with Same Row or Column
#On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

#A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

#Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

 

#Example 1:

#Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
#Output: 5
#Explanation: One way to remove 5 stones is as follows:
#1. Remove stone [2,2] because it shares the same row as [2,1].
#2. Remove stone [2,1] because it shares the same column as [0,1].
#3. Remove stone [1,2] because it shares the same row as [1,0].
#4. Remove stone [1,0] because it shares the same column as [0,0].
#5. Remove stone [0,1] because it shares the same row as [0,0].
#Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        time O(n), space O(n * n)
        
        """
        rowTable, colTable = defaultdict(set), defaultdict(set)
        
        for i, (row, col) in enumerate(stones):
            rowTable[row].add(i)
            colTable[col].add(i)
        
        graph = defaultdict(set)
        for i, (row, col) in enumerate(stones): 
            graph[i] = rowTable[row].union(colTable[col])
            graph[i].remove(i)
            
        visited = set()
                
        def dfs(stone_idx):
            nonlocal graph, visited
            if stone_idx in visited:
                return
            
            visited.add(stone_idx)
            for next_stone in graph[stone_idx]:
                if next_stone not in visited:
                    dfs(next_stone)
        
        stone_left = 0
        print(graph)
        for stone_idx in range(len(stones)):
            if stone_idx not in visited:
                dfs(stone_idx)
                stone_left += 1
        return len(stones) - stone_left
        
            
            
            
        
        
        
        