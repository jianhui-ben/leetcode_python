# 1584. Min Cost to Connect All Points
# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
#
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
#
# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.


class UF:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.sizes = [1 for _ in range(size)]
        self.numOfGroups = size

    def union(self, a, b):
        a_root, b_root = self.find(a), self.find(b)
        if a_root == b_root: return
        if self.sizes[a_root] < self.sizes[b_root]:
            a_root, b_root = b_root, a_root
        self.parents[b_root] = a_root
        self.sizes[a_root] += self.sizes[b_root]
        self.numOfGroups -= 1

    def find(self, a):
        while self.parents[a] != a:
            self.parents[a] = self.parents[self.parents[a]]
            a = self.parents[a]
        return a

    def allConnected(self):
        return self.numOfGroups == 1

    def connected(self, a, b):
        return self.find(a) == self.find(b)


import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ## minimum spanning tree
        distanceHeap = []

        def dis(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1 - x2) + abs(y1 - y2)

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                distanceHeap.append((dis(points[i], points[j]), i, j))

        heapq.heapify(distanceHeap)
        out, uf = 0, UF(len(points))
        while distanceHeap and not uf.allConnected():
            distance, i, j = heapq.heappop(distanceHeap)
            if uf.connected(i, j):
                continue
            uf.union(i, j)
            out += distance

        return out
