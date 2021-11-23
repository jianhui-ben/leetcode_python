# 952. Largest Component Size by Common Factor
# You are given an integer array of unique positive integers nums. Consider the following graph:
#
# There are nums.length nodes, labeled nums[0] to nums[nums.length - 1],
# There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
# Return the size of the largest connected component in the graph.

class uf:
    def __init__(self, size):
        self.parent = [i for i in range((size))]
        self.size = [1 for _ in range(size)]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root: return
        if self.size[x_root] >= self.size[y_root]:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
        else:
            self.parent[x_root] = y_root
            self.size[y_root] += self.size[x_root]

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        """
        union find
        how to quickly find num1 and num2 have common factor

        for every num, we have factors_set
        if len(set.union(num1's factors_set, num2's factors_set))> len1 + len2: union num1 and num2
        """

        def decompose(num):
            factor = 2
            res = []
            while num >= factor * factor:
                if num % factor == 0:
                    res.append(factor)
                    num = num // factor
                else:
                    factor += 1
            res.append(num)
            return res

        union_find = uf(max(nums) + 1)
        for num in nums:
            prime_factors = decompose(num)
            for factor in prime_factors:
                union_find.union(num, factor)

        groups, max_size = defaultdict(int), 0
        for num in nums:
            groups[union_find.find(num)] += 1
            max_size = max(max_size, groups[union_find.find(num)])

        return max_size