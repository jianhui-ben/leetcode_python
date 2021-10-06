#Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

#You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

#Example 1:

#Input: nums = [4,3,2,7,8,2,3,1]
#Output: [2,3]
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ## negation method
        out = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= -1
            else:
                out.append(abs(nums[i]))
        return out
        
        
#         ## swapping
#         nums = [0] + nums
        
#         for i in range(1, len(nums)):
#             while nums[i] != i and nums[i] != nums[nums[i]]:
#                 temp = nums[i]
#                 nums[i], nums[temp] = nums[temp], nums[i]
            
#         return [v for i, v in enumerate(nums) if i != v]
        