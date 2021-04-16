#261. Graph Valid Tree
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ## approach 2:
        ## in graph theory, for a graph to be a valid tree, it must have exactly n-1 edges and it can't be fully connected. So if the graph is fully connected and contains exactly n-1 edges,it can't possibly contain a cycle, so it must be a tree
        ## O(n), O(n)
        if len(edges)!=n-1: return False
        if n==0: return False
        stored = defaultdict(list)
        for a,b in edges:
            stored[a].append(b)
            stored[b].append(a)
        
        def dfs(node, seen):
            seen.add(node)
            for neigh in stored[node]:
                if neigh not in seen:
                    dfs(neigh, seen)
        seen= set()
        dfs(0, seen)
        return len(seen)==n
        
        
        
        
        
        
        
        
        
        
        
        ## approach 1
        ## adjancency list + dfs
        ## check if one node connect to all nodes, and if there's a cycle
        ## time O(N + E), space O(n+e)
        
        if n==0: return False
        stored = defaultdict(list)
        for a,b in edges:
            stored[a].append(b)
            stored[b].append(a)
        
#         def check_fully_connected(cur_node, stored, path):
#             path.add(cur_node)
#             for next_node in stored[cur_node]:
#                 if next_node not in path:
#                     check_fully_connected(next_node, stored, path)
        
#         seen= set()
#         check_fully_connected(0, stored, seen)
#         if len(seen)<n: return False
        
        ## check if cycle occurs   
        def dfs(parent_node, cur_node, stored, path):
            if cur_node in path:
                return False
            path.add(cur_node)
            for next_node in stored[cur_node]:
                if next_node == parent_node:
                    continue
                if not dfs(cur_node, next_node, stored, path):
                    return False
            return True
        seen = set()
        if not dfs(None, 0, stored, seen): return False
        else: return len(seen)== n

