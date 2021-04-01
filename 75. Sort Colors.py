#75. Sort Colors
#Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

 

#Example 1:

#Input: nums = [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## two pointer
        ## Dutch National Flag Problem (check the solution)
        ## 0 to left, 2 to right
        i, left, right=0, 0, len(nums)-1
        
        while i<=right:
            if nums[i]==0:
                nums[left], nums[i]= nums[i], nums[left]
                left+=1
                i+=1
            elif nums[i]==2:
                nums[i], nums[right]= nums[right], nums[i]
                right-=1
            else:
                i+=1