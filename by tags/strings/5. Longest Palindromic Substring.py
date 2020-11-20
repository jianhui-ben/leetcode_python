#5. Longest Palindromic Substring
#Given a string s, return the longest palindromic substring in s.

#Example 1:

#Input: s = "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.
#Example 2:

#Input: s = "cbbd"
#Output: "bb"

class Solution:
    ## brute force
    def longestPalindrome(self, s: str) -> str:
        if not s: return None
        if len(s)==1: return s
        dp= [[False]*len(s) for _ in range(len(s))]
        ans=(0, 0)
        for column in range(len(s)):
            for row in range(column, -1, -1):
                if row==column:
                    dp[row][column]=True
                elif column==row+1:
                    dp[row][column]=  s[row]==s[column]
                else:
                    dp[row][column]= dp[row+1][column-1] and (s[row]==s[column])
                if dp[row][column] and column-row>= ans[1]-ans[0]:
                    # print(column-row)
                    ans= (row, column)
        # print(dp)
        return s[ans[0]:ans[1]+1]

