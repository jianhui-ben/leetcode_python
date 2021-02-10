#55. Jump Game

#Given an array of non-negative integers, you are initially positioned at 
#the first index of the array.

#Each element in the array represents your maximum jump length at that position.

#Determine if you are able to reach the last index.

#Example 1:

#Input: nums = [2,3,1,1,4]
#Output: true
#Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1: return True
        if (not nums) or nums[0]== 0: return False
        furthest= 1
        i, furthest =0, nums[0]
        while i<= furthest and i<len(nums)-1:
            furthest= max(i+ nums[i], furthest)
            if furthest>=len(nums)-1:return True
            i+=1
        return False
