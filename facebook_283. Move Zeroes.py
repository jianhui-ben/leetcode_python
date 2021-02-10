#283. Move Zeroes

#Given an array nums, write a function to move all 0's
#to the end of it while maintaining the relative order of the non-zero elements.

#Example:

#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
#Note:

#You must do this in-place without making a copy of the array.
#Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ##brute force
        # counts= nums.count(0)
        # while 0 in nums: nums.remove(0)
        # nums+=[0]*counts
        
        ## two pointer (swapping)
        if not nums: return None
        anchor, explore= 0, 0
        while explore <len(nums):
            if nums[explore]!=0 and explore!=anchor:
                temp= nums[anchor]
                nums[anchor]=nums[explore]
                nums[explore]=temp
            if nums[anchor]!= 0:
                anchor+=1
            explore+=1
