#213. House Robber II

#You are a professional robber planning to rob houses along a street. 
#Each house has a certain amount of money stashed. All houses at this 
#place are arranged in a circle. That means the first house is the neighbor 
#of the last one. Meanwhile, adjacent houses have a security system connected,
#and it will automatically contact the police if two adjacent houses were broken 
#into on the same night.

#Given a list of non-negative integers nums representing the amount of money 
#of each house, return the maximum amount of money you can rob
#tonight without alerting the police.

 

#Example 1:

#Input: nums = [2,3,2]
#Output: 3
#Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), 
#because they are adjacent houses.


class Solution:
    
    def rob_linear(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        elif len(nums)<=2:
            return max(nums)
        dp= [0 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            if i==0:
                dp[i]= nums[0]
            elif i==1:
                dp[i]= max(dp[i-1], nums[i])
            else:
                dp[i]= max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]
    
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        elif len(nums)<=2:
            return max(nums)
        return max(self.rob_linear(nums[:-1]), 
                  self.rob_linear(nums[1:]))