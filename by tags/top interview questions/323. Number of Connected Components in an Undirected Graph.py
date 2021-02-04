#323. Number of Connected Components in an Undirected Graph
#Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

#Example 1:

#Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

#     0          3
#     |          |
#     1 --- 2    4 

#Output: 2
#Example 2:

#Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

#     0           4
#     |           |
#     1 --- 2 --- 3

#Output:  1
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ##hashtable dfs
        if not edges: return n
        stored= collections.defaultdict(set)
        for a, b in edges:
            stored[a].add(b)
            stored[b].add(a)
        
        visited=set()
        count=0
        
        def dfs(cur_node, stored, visited):
            visited.add(cur_node)
            for next_node in stored[cur_node]:
                if next_node not in visited:
                    dfs(next_node, stored, visited)

        for i in range(n):
            if i not in visited:
                dfs(i, stored, visited)
                count+=1
            
        return count

        
        