# 334. Increasing Triplet Subsequence
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """

        [2, 1,2, 5, 0, 4, 6]
            ^
                          ^

        start, end
        left += 1, if nums[left] <=start: start = nums[left]
        right -= 1, if nums[right] >= end: end = nums[right]


        5,4,3,2,1


        [1, 2, 45, 0, 2]
         ^
               ^

        [45, 47, 1]




        [1,2, 45, 1, 2]
           ^
                     ^
        start = 0, end = 4

        two pointer
        """
        left, right = 0, len(nums) - 1
        while left + 1 < right and nums[left + 1] <= nums[left]:
            left += 1

        while right - 1 > left and nums[right - 1] >= nums[right]:
            right -= 1

        start, end = left, right
        temp_left, temp_right = left, right
        while temp_left < temp_right:
            if nums[start] < nums[temp_left] < nums[end]:
                return True
            if nums[temp_left] <= nums[start]:
                start = temp_left
            temp_left += 1

        start, end = left, right
        temp_left, temp_right = left, right
        while temp_left < temp_right:
            if nums[start] < nums[temp_right] < nums[end]:
                return True
            if nums[temp_right] >= nums[end]:
                end = temp_right
            temp_right -= 1
        return False
