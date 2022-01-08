# 793. Preimage Size of Factorial Zeroes Function
#
# Let f(x) be the number of zeroes at the end of x!. Recall that x! = 1 * 2 * 3 * ... * x and by convention, 0! = 1.
#
# For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has two zeroes at the end.
# Given an integer k, return the number of non-negative integers x have the property that f(x) = k.
#
#
#
# Example 1:
#
# Input: k = 0
# Output: 5
# Explanation: 0!, 1!, 2!, 3!, and 4! end with k = 0 zeroes.


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        """
        binary search + trailing zero in 172
        find left and right boundary in binary search in range(0, (k+1) * 5)
        time: log k * log k
        """

        def trailingZero(n):
            out = 0
            while n >= 5:
                out += n // 5
                n = n // 5
            return out

        left, right = 0, 5 * (k + 1)

        while left <= right:
            mid = left + (right - left) // 2
            if trailingZero(mid) >= k:
                right = mid - 1
            else:
                left = mid + 1

        final_left = left

        left, right = 0, 5 * (k + 1)

        while left <= right:
            mid = left + (right - left) // 2
            if trailingZero(mid) > k:
                right = mid - 1
            else:
                left = mid + 1

        final_right = right

        return final_right - final_left + 1

