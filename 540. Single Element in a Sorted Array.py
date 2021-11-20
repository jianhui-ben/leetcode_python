# 540. Single Element in a Sorted Array
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
#
# Return the single element that appears only once.
#
# Your solution must run in O(log n) time and O(1) space.

#
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        binary search
        if nums[i-1] != nums[i] != nums[i + 1]: return nums[i]
        assuming nums[i] == nums[i+1] and i %2 == 0: go to right
        assuming nums[i]==nums[i-1] and i%2==1: go to right

        assuming nums[i] == nums[i+1] and i%2===1: go to left
        assuming nums[i]==nums[i-1] and i%2==1: go to left

        [1,1,2,3,3,4,4,8,8]
        left: 0 right: 8
        mid: 4

        """
        if len(nums) == 1: return nums[0]

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if (mid == 0 and nums[mid] != nums[mid + 1]) or \
                    (mid == len(nums) - 1 and nums[mid - 1] != nums[mid]) or \
                    (nums[mid - 1] != nums[mid] != nums[mid + 1]):
                return nums[mid]

            elif nums[mid] == nums[mid + 1] and mid % 2 == 0:
                left = mid + 2
            elif nums[mid] == nums[mid - 1] and mid % 2 == 1:
                left = mid + 1
            elif nums[mid] == nums[mid + 1] and mid % 2 == 1:
                right = mid - 1
            elif nums[mid] == nums[mid - 1] and mid % 2 == 0:
                right = mid - 2

        return -1

