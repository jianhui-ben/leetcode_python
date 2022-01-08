## this is for github test

##Given an array of integers, return indices of the two numbers such 
#that they add up to a specific target.
#You may assume that each input would have exactly one solution, 
#and you may not use the same element twice.

#example:

#given nums = [2, 7, 11, 15], target = 9,
#because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i, x in enumerate(nums):
            find=target-x
            if find in nums and i!=nums.index(find):
                return [i, nums.index(find)]
        return []

"""
[5, 3, 2, 1, 66]




"""











