#368. Largest Divisible Subset

#Given a set of distinct positive integers nums, return the largest subset answer such that every pair 
#(answer[i], answer[j]) of elements in this subset satisfies:

#answer[i] % answer[j] == 0, or
#answer[j] % answer[i] == 0
#If there are multiple solutions, return any of them.

#Example 1:

#Input: nums = [1,2,3]
#Output: [1,2]
#Explanation: [1,3] is also accepted.
#Example 2:

#Input: nums = [1,2,4,8]
#Output: [1,2,4,8]


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        dp
        hint: 
        in a sorted arr [A, B, C] which satisfy the requirements
        if D % C ==0 then [A, B, C, D] satisfy the requirements
        
        dp[i] = list which satisfy the requirement ending nums[i]
        for j in range(i):
           if nums[i]%nums[j] == 0 and len(dp[j] + 1) > len(dp[i]):
                dp[i] = dp[j] + [nums[i]]
                
        3 4 8 16
        dp[1] 4
        dp[2] 4, 8
        dp[3] 4, 
        
        """
        nums.sort()
        dp = [[i] for i in nums]
        
        for i in range(1, len(dp)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
        
        max_len, output = 0, None
        for l in dp:
            if len(l) > max_len:
                max_len = len(l)
                output = l
                
        return output