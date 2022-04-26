# There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.
#
# A critical connection is a connection that, if removed, will make some servers unable to reach some other server.
#
# Return all critical connections in the network in any order.

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(set)
        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)
        # print(graph)
        ranks = {}

        def dfs(cur_i, cur_rank):
            # print(ranks)
            if cur_i in ranks:
                return ranks[cur_i]

            ranks[cur_i] = cur_rank
            next_options = graph[cur_i]
            min_rank = cur_rank + 1
            for next_i in list(next_options):
                if next_i in ranks and ranks[next_i] == cur_rank - 1:
                    continue
                min_next_rank = dfs(next_i, cur_rank + 1)
                if min_next_rank <= cur_rank:
                    graph[cur_i].remove(next_i)
                    graph[next_i].remove(cur_i)
                    min_rank = min(min_rank, min_next_rank)
            return min_rank

        dfs(0, 0)

        out = []
        for i in range(n):
            for j in list(graph[i]):
                out.append([i, j])
                graph[j].remove(i)

        return out


