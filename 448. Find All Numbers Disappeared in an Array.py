#448. Find All Numbers Disappeared in an Array
#Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

#Example 1:

#Input: nums = [4,3,2,7,8,2,3,1]
#Output: [5,6]
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        """
        4,3,2,7,8,2,3,1
        -1,-2,-3,-4,3,2,-7,-8
        cur = 4
        inplace swapping
        """
        for i in range(len(nums)):
            
            while nums[i] > 0 and nums[(nums[i] - 1)] > 0:
                temp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[temp - 1] = - temp
        
        out = []
        for i in range(len(nums)):
            if i + 1 != - nums[i]:
                out.append(i + 1)
        return out
            
                