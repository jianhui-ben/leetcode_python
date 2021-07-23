#915. Partition Array into Disjoint Intervals
#Given an array nums, partition it into two (contiguous) subarrays left and right so that:

#Every element in left is less than or equal to every element in right.
#left and right are non-empty.
#left has the smallest possible size.
#Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

 

#Example 1:

#Input: nums = [5,0,3,8,6]
#Output: 3
#Explanation: left = [5,0,3], right = [8,6]


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        """
        genius approach: one loop O(n), O(1)
        """
        temp_max, left_max = nums[0], nums[0]
        out = 1
        
        for i, n in enumerate(nums[1:], 1):
            temp_max = max(temp_max, n)
            if n < left_max:
                out = i + 1
                left_max = temp_max
        return out
        
        """
        temp: 5, leftmax: 5
        
        out = 2
        
        """
        
        
        """
        max(left) <= min(right)
        time O(n), space O(n)
        """
        max_left, min_right = [None] * len(nums), [None] * len(nums)
        max_left[0], min_right[-1] = nums[0], nums[-1]
        for i in range(1, len(nums)):
            max_left[i] = max(max_left[i - 1], nums[i])
        
        for i in range(len(nums) - 2, -1, -1):
            min_right[i] = min(min_right[i + 1], nums[i])
        
        # print(max_left)
        # print(min_right)
        for i in range(len(nums) - 1):
            if max_left[i] <= min_right[i + 1]:
                return i + 1