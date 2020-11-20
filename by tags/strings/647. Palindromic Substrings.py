#647. Palindromic Substrings
#Given a string, your task is to count how many palindromic substrings in this string.

#The substrings with different start indexes or end indexes are counted 
#as different substrings even they consist of same characters.

#Example 1:

#Input: "abc"
#Output: 3
#Explanation: Three palindromic strings: "a", "b", "c".


class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s: return 0
        if len(s)==1: return 1
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
        return sum([sum(i) for i in dp])
