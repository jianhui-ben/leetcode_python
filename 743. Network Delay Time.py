# 743. Network Delay Time
# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
#
# We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.


import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        BFS djikstra algorithm
        """
        graph = defaultdict(set)
        for time in times:
            graph[time[0]].add((time[1], time[2]))

        queue, storedDisFromK = [(0, k)], [float('inf') for _ in range(n + 1)]
        storedDisFromK[0] = 0
        while queue:

            cur_dis, cur_node = heapq.heappop(queue)

            if storedDisFromK[cur_node] <= cur_dis:
                continue
            storedDisFromK[cur_node] = cur_dis

            for next_node, next_dis in graph[cur_node]:
                if next_dis + cur_dis < storedDisFromK[next_node]:
                    heapq.heappush(queue, (next_dis + cur_dis, next_node))
        out = max(storedDisFromK)
        return out if out != float('inf') else -1






