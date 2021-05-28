#1218. Longest Arithmetic Subsequence of Given Difference
#Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

#A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.

 

#Example 1:

#Input: arr = [1,2,3,4], difference = 1
#Output: 4
#Explanation: The longest arithmetic subsequence is [1,2,3,4].

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ##  dp[i]: longest subsequence up to arr[i]
        ## dp[i]= max(dp[i-1], stored[ar[i]-dif]+1)
        ## stored[arr[i]] = max(stored[arr[i]], stored[ar[i]-dif]+1)
        ## stored the length of longest subsequence ending with value arr[i]
        ## return dp[-1]
        
#         ## O(n) and O(n) dp
#         dp= [None] * len(arr)
#         dp[0]=1
#         stored = defaultdict(lambda:1)
#         stored[arr[0]] = 1
#         for i in range(1, len(dp)):
#             if (arr[i]-difference) in stored:
#                 dp[i] = max(dp[i-1], 1+ stored[arr[i]-difference])
#                 stored[arr[i]] =max(stored[arr[i]], 1+ stored[arr[i]-difference])
#             else:
#                 dp[i] = dp[i-1]
#                 stored[arr[i]] =1
            
#         return dp[-1]
        
        ## hashmap, just store the longest length ending with value arr[i]
        stored = defaultdict(lambda:1)
        stored[arr[0]] = 1
        for i in range(1, len(arr)):
            if (arr[i]-difference) in stored:
                stored[arr[i]] =max(stored[arr[i]], 1+ stored[arr[i]-difference])
            else:
                stored[arr[i]] =1
            
        return max([v for _, v in stored.items()])

        
