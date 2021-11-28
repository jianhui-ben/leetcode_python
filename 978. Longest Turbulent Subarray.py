# 978. Longest Turbulent Subarray
# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.
#
# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
#
# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:
#
# For i <= k < j:
# arr[k] > arr[k + 1] when k is odd, and
# arr[k] < arr[k + 1] when k is even.
# Or, for i <= k < j:
# arr[k] > arr[k + 1] when k is even, and
# arr[k] < arr[k + 1] when k is odd.

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        sliding window
        """
        out, left = 1, 0
        for i in range(1, len(arr)):
            # print(i, left)
            cur_dif = arr[i] - arr[i - 1]
            if cur_dif == 0:
                left = i
            out = max(out, i - left + 1)
            if i == len(arr) - 1 or cur_dif * (arr[i + 1] - arr[i]) >= 0:
                left = i

        return out

#         """
#         track the first two element's comparison
#         cur_max = 2
#         if the third follow the rules:
#         cur_max += 1
#         else:
#         cur_max = 2

#         out = max(cur_max, out)
#         """
#         cur_dif, cur_max, out = None, 1, 1
#         for i in range(1, len(arr)):
#             if arr[i] == arr[i - 1]:
#                 cur_dif, cur_max = None, 1
#                 continue
#             if cur_dif == None:
#                 cur_dif = arr[i] - arr[i - 1]
#                 cur_max += 1
#             else:
#                 if cur_dif * (arr[i] - arr[i-1]) < 0:
#                     cur_max += 1
#                 elif cur_dif * (arr[i] - arr[i-1]) > 0:
#                     cur_max = 2
#                 cur_dif = arr[i] - arr[i - 1]
#             out = max(cur_max, out)
#         return out




