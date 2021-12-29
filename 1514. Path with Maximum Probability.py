# 1514. Path with Maximum Probability
#
# You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].
#
# Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.
#
# If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.
#

import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        """
        typical dijkstra algorithm
        """

        ## create a graph
        graph = defaultdict(list)
        for i in range(len(edges)):
            prob = succProb[i]
            graph[edges[i][0]].append((edges[i][1], prob))
            graph[edges[i][1]].append((edges[i][0], prob))

        queue, stored = [(-1, start)], [float('-inf') for _ in range(n)]
        stored[start] = 1

        while queue:
            cur_prob, cur_node = heapq.heappop(queue)

            if cur_node == end:
                return abs(cur_prob)
            if abs(cur_prob) < stored[cur_node]:
                continue
            stored[cur_node] = abs(cur_prob)

            for next_node, next_prob in graph[cur_node]:
                if stored[next_node] < cur_prob * next_prob:
                    heapq.heappush(queue, (cur_prob * next_prob, next_node))

        return 0


