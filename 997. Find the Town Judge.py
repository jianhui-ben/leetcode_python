# 997. Find the Town Judge
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
#
# If the town judge exists, then:
#
# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
#
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
#
#

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        store = [1] * n
        for pair in trust:
            store[pair[0] - 1] = 0
            store[pair[1] - 1] += 1

        for i, v in enumerate(store):
            if v == n: return i + 1
        return -1
