# 1135. Connecting Cities With Minimum Cost
# There are n cities labeled from 1 to n. You are given the integer n and an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.
#
# Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1,
#
# The cost is the sum of the connections' costs used.

class UF:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1 for _ in range(n)]

    def union(self, a, b):
        a_root, b_root = self.find(a), self.find(b)
        if self.sizes[a_root] < self.sizes[b_root]:
            a_root, b_root = b_root, a_root
        self.parents[b_root] = a_root
        self.sizes[a_root] += self.sizes[b_root]

    def find(self, a):
        while self.parents[a] != a:
            self.parents[a] = self.parents[self.parents[a]]
            a = self.parents[a]
        return a

    def connected(self, a, b):
        return self.find(a) == self.find(b)


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        """
        union find + greedy
        """
        connections = sorted(connections, key=lambda x: x[2])

        uf, out = UF(n + 1), 0
        for edge in connections:
            if uf.connected(edge[0], edge[1]):
                continue
            uf.union(edge[0], edge[1])
            out += edge[2]
        return out if uf.sizes[uf.find(1)] == n else -1

