#300. Longest Increasing Subsequence
#Given an unsorted array of integers, find the length of longest increasing subsequence.

#Example:

#Input: [10,9,2,5,3,7,101,18]
#Output: 4 
#Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
#Note:

#There may be more than one LIS combination, it is only necessary for you to return the length.
#Your algorithm should run in O(n2) complexity.
#Follow up: Could you improve it to O(n log n) time complexity?



class Solution:
    ##dp solution: O(N*2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        dp=[1]* len(nums)
        for i in range(1, len(nums)):
            for k in range(i):
                if nums[k]<nums[i]:
                    dp[i]=max(dp[i], dp[k]+1)
        return max(dp)
    
    
    ##there could be a better way of using dp and binary search to make the run time to O(n log n)
