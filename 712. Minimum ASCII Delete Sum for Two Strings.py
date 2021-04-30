#712. Minimum ASCII Delete Sum for Two Strings
#Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

#Example 1:
#Input: s1 = "sea", s2 = "eat"
#Output: 231
#Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
#Deleting "t" from "eat" adds 116 to the sum.
#At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        ## dp         
        ## time O(MN), space O(MN)
        num_s1, num_s2 = [ord(i) for i in s1], [ord(i) for i in s2]
        
        dp=[[0 for _ in range(len(num_s2)+1)] for _ in range(len(num_s1)+1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i==0:
                    dp[i][j]=sum(num_s2[:j])
                elif j==0:
                    dp[i][j]=sum(num_s1[:i])  
                elif num_s1[i-1]==num_s2[j-1]:
                    dp[i][j]= dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+num_s1[i-1] , dp[i][j-1]+num_s2[j-1])
        return dp[-1][-1]        