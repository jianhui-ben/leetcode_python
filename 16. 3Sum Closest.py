#16. 3Sum Closest
#Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

#Example 1:

#Input: nums = [-1,2,1,-4], target = 1
#Output: 2
#Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        assuming we have 0<i<j<k<len(nums)
        traverse nums to fix i
        two pointer to find left and right closest to target -nums[i]
        
        O(n**2) time, O(1) space
        """
        nums.sort()
        out = float('inf')
        
        for i in range(len(nums) - 2):
            two_sum = target - nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == two_sum:
                    return target
                
                if abs(out - target) > abs(two_sum - nums[left] - nums[right]):
                    out = nums[i] + nums[left] + nums[right]
                
                if nums[left] + nums[right] > two_sum:
                    right -= 1
                else:
                    left += 1
        return out
        