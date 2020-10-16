#152. Maximum Product Subarray

#Given an integer array nums, find the contiguous subarray within an array 
#(containing at least one number) which has the largest product.

#Example 1:

#Input: [2,3,-2,4]
#Output: 6
#Explanation: [2,3] has the largest product 6.
#Example 2:

#Input: [-2,0,-1]
#Output: 0
#Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

##dynamic programming
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums)==1:
            return nums[0]
        dp, small, large=[_ for _ in range(len(nums))], [_ for _ in range(len(nums))], [_ for _ in range(len(nums))]
        dp[0], small[0], large[0]= nums[0],nums[0],nums[0]
        for i in range(1, len(nums)):
            large[i]= max([large[i-1]*nums[i], small[i-1]*nums[i], nums[i]])
            small[i]= min([large[i-1]*nums[i], small[i-1]*nums[i], nums[i]])
            dp[i]= large[i]
            
        return max(dp)


