#516. Longest Palindromic Subsequence
#Given a string s, find the longest palindromic subsequence's length in s.

#A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

#Example 1:

#Input: s = "bbbab"
#Output: 4
#Explanation: One possible longest palindromic subsequence is "bbbb".



class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ## subsequence always use dp
        ## 2D DP tables dp[i][j] contains the length of LPS in s[i:j+1], where 0<=i<=len(s)-1, 0<=j<=len(s)-1
        ## status change:

        ## O(n**2), O(n**2)
            
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(dp)-1, -1, -1):
            for j in range(i, len(dp)):
                if i>j: continue
                elif i==j: dp[i][j]=1
                elif s[i]==s[j]: 
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]
        