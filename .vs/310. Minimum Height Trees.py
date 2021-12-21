# 310. Minimum Height Trees
# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.
#
# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
#
# Return a list of all MHTs' root labels. You can return the answer in any order.
#
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        topological sort
        until checked nodes >= n - 1
        """
        if n == 1: return [0]
        degrees = [0 for _ in range(n)]
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            degrees[edge[0]] += 1
            degrees[edge[1]] += 1

        queue, checked = [i for i, degree in enumerate(degrees) if degree == 1], 0

        while queue and checked < n - 2:
            temp = []

            for cur_node in queue:
                checked += 1
                for next_node in graph[cur_node]:
                    degrees[next_node] -= 1
                    if degrees[next_node] == 1:
                        temp.append(next_node)
            queue = temp

        return queue