# 1202. Smallest String With Swaps
# You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
#
# You can swap the characters at any pair of indices in the given pairs any number of times.
#
# Return the lexicographically smallest string that s can be changed to after using the swaps.
#
#
#
# Example 1:
#
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination:
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"

from collections import defaultdict
import heapq

class UF:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.sizes = [1 for _ in range(size)]

    def union(self, a, b):
        a_root, b_root = self.find(a), self.find(b)
        if a_root == b_root: return
        if self.sizes[a_root] < self.sizes[b_root]:
            a_root, b_root = b_root, a_root
        self.parents[b_root] = a_root
        self.sizes[a_root] += self.sizes[b_root]
        return

    def find(self, a):
        while self.parents[a] != a:
            self.parents[a] = self.parents[self.parents[a]]
            a = self.parents[a]
        return a

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        """
        union find to separate index with groups
        sort each group
        """
        uf, groups = UF(size=len(s)), defaultdict(list)
        for pair in pairs:
            uf.union(pair[0], pair[1])

        for i in range(len(s)):
            heapq.heappush(groups[uf.find(i)], s[i])

        out = ""
        for i in range(len(s)):
            out += heapq.heappop(groups[uf.find(i)])

        return out
