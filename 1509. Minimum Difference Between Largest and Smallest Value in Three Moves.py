#1509. Minimum Difference Between Largest and Smallest Value in Three Moves
#Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.

#Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.

 

#Example 1:

#Input: nums = [5,3,2,4]
#Output: 0
#Explanation: Change the array [5,3,2,4] to [2,2,2,2].
#The difference between the maximum and minimum is 2-2 = 0.
#Example 2:

#Input: nums = [1,5,0,10,14]
#Output: 1
#Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
#The difference between the maximum and minimum is 1-0 = 1.
#Example 3:

#Input: nums = [6,6,0,1,1,4,6]
#Output: 2
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        """
        
        6,6,0,1,1,4,6
        
        0 1 1 4 6 6 6
        
        i: 0 -- > out: nums[7 - 4 + 0] - nums[0] = 4
        i: 1 -- > out: nums[7-4+1]
        
        
        """
        if len(nums) <= 4: 
            return 0
        
        nums.sort()
        
        out = float('inf')
        for i in range(4):
            
            out = min(out, nums[len(nums) - 4 + i] - nums[i])
        
        return out