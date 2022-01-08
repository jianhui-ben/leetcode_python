# 1010. Pairs of Songs With Total Durations Divisible by 60
#
# You are given a list of songs where the ith song has a duration of time[i] seconds.
#
# Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
#
#
#
# Example 1:
#
# Input: time = [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
from collections import Counter


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        20, 30, 40, 100, 150

        20, 30, 40, 40, 30

        20, 30, 30, 40, 40
        ^               ^

        20, 30, 40

        20: 1
        30: 2
        40: 2

        1 * 2 + (store[30] * store[30] - 1) + (store[0] * store[0] - 1)

        """

        store = Counter([i % 60 for i in time])
        unique_time = sorted(list(store.keys()))
        out, left, right = 0, 0, len(unique_time) - 1
        while left < right:
            left_time, right_time = unique_time[left], unique_time[right]
            if left_time == 0:
                left += 1
            elif right_time == 60:
                right -= 1
            elif left_time + right_time == 60:
                out += store[left_time] * store[right_time]
                left += 1
                right -= 1
            elif left_time + right_time < 60:
                left += 1
            else:
                right -= 1
        if store[30] > 1: out += (store[30] * (store[30] - 1)) / 2
        if store[0] > 1: out += (store[0] * (store[0] - 1)) / 2

        return int(out)