# 2007. Find Original Array From Doubled Array
# An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.
#
# Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        """
        1, len(changed) = even
        2, the changed can be split into 2 equal length list: once and twice
        assign each element to once or twice


        [1,3,4,2,6,8]
        once:  1,
        twice: 2,

        sort:
        1,2,3,4,6,8
        1: can only be with 2
        from left to right: find the right number. = 2* left
        if couldn't find: return []
        be careful about 0
        """
        if len(changed) % 2: return []
        changed.sort()
        stored_idx = defaultdict(list)
        for i, val in enumerate(changed):
            stored_idx[val].append(i)
        visited, out = set(), []
        if len(stored_idx[0]) % 2:
            return []
        else:
            out = [0 for _ in range(len(stored_idx[0]) // 2)]
            stored_idx.pop(0)
        for small_i, small in enumerate(changed):
            if small_i in visited or not small:
                continue
            visited.add(small_i)
            large = small * 2
            if not len(stored_idx[large]):
                return []
            visited.add(stored_idx[large].pop())
            out.append(small)

        return out
