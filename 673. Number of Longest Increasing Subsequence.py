#673. Number of Longest Increasing Subsequence
#Given an integer array nums, return the number of longest increasing subsequences.

#Notice that the sequence has to be strictly increasing.

 

#Example 1:

#Input: nums = [1,3,5,4,7]
#Output: 2
#Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
#Example 2:

#Input: nums = [2,2,2,2,2]
#Output: 5
#Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        """
        dp
        dp[i]: the number of longest increases subsequences with nums[i] as the ending and the length of the longest subsequences
        return dp[-1][0]
        
        for j in range(i):
            if nums[i]>nums[j]:
               if dp[j][1] +1 > dp[i][1]:
                   dp[i][1] =  dp[j][1] + 1
                   dp[i][0] = dp[j][0]
                elif dp[j][1] + 1 == dp[i][1]:
                    dp[i][0] += dp[j][0]        
        """
        
        dp = [(1, 1)] * len(nums)
        dp[0] = (1, 1)
        
        
        #[2,2,2,2,2]
        
        ##[1,2,4,3,5,4,7,2]
        
        max_len = 1
        
        for i in range(1, len(dp)):

            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    if dp[j][1] + 1 > dp[i][1]:
                        dp[i] = (dp[j][0], dp[j][1] + 1)
                    elif dp[j][1] + 1 == dp[i][1]:
                        dp[i] = ((dp[i][0] + dp[j][0]), dp[i][1])
            max_len = max(max_len, dp[i][1])
        
        out= 0
        for cnt, len_ in dp:
            if len_ == max_len:
                out += cnt
        # print(dp)
        
        
        return out        
#         (2, 3), (2, 3)
#         3+ 1> 3: dp[i] = (2, 3+1)

        
        
        
        
        
        
        
        
        
        
        

