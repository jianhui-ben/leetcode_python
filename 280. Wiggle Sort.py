#280. Wiggle Sort
#Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

#You may assume the input array always has a valid answer.

 

#Example 1:

#Input: nums = [3,5,2,1,6,4]
#Output: [3,5,1,6,2,4]
#Explanation: [1,6,2,5,3,4] is also accepted.


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## swap method
        
        if len(nums) < 2: return
        
        for i in range(len(nums) - 1):
            
            if i % 2 == 0:
                
                if nums[i + 1] < nums[i]:
                    
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    
            else:
                
                if nums[i + 1] > nums[i]:
                    
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    
        return
