# 710. Random Pick with Blacklist
#
# You are given an integer n and an array of unique integers blacklist. Design an algorithm to pick a random integer in the range [0, n - 1] that is not in blacklist. Any integer that is in the mentioned range and not in blacklist should be equally likely to be returned.
#
# Optimize your algorithm such that it minimizes the number of calls to the built-in random function of your language.
#
# Implement the Solution class:
#
# Solution(int n, int[] blacklist) Initializes the object with the integer n and the blacklisted integers blacklist.
# int pick() Returns a random integer in the range [0, n - 1] and not in blacklist.

import random


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.stored = {}
        self.size, last = n - len(blacklist), n - 1
        check = set(blacklist)
        for i in blacklist:
            if i >= self.size:
                continue
            while last in check:
                last -= 1
            self.stored[i] = last
            last -= 1

    def pick(self) -> int:
        cur_i = random.randrange(0, self.size)
        if cur_i in self.stored:
            return self.stored[cur_i]
        return cur_i

        return self.stack[random.randrange(0, len(self.stack))]

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()