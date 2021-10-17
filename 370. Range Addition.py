# 370. Range Addition
# You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].
#
# You have an array arr of length length with all zeros, and you have some operation to apply on arr. In the ith operation, you should increment all the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.
#
# Return arr after applying all the updates.


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        """
        brainteaser prefix sum

        [0, 2, 7, 2, 0]

        [1, 3, 2]


        """
        res = [0] * length

        for start, end, inc in updates:
            res[start] += inc
            if end + 1 < length:
                res[end + 1] -= inc

        for i in range(1, length):
            res[i] += res[i - 1]

        return res
