# 886. Possible Bipartition
# We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.
#
# Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(set)

        for dis in dislikes:
            graph[dis[0]].add(dis[1])
            graph[dis[1]].add(dis[0])

        visited, out = {}, True

        def traverse(person, group):
            nonlocal out
            visited[person] = group
            for next_p in graph[person]:
                if next_p not in visited:
                    traverse(next_p, not group)
                elif visited[next_p] == group:
                    out = False
                if out == False:
                    return
