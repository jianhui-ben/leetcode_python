#1143. Longest Common Subsequence
#Given two strings text1 and text2, return the length of their longest common subsequence.

#A subsequence of a string is a new string generated from the original string with 
#some characters(can be none) deleted without changing the relative order of the remaining 
#characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence 
#of two strings is a subsequence that is common to both strings.

#If there is no common subsequence, return 0.

#Example 1:

#Input: text1 = "abcde", text2 = "ace" 
#Output: 3  
#Explanation: The longest common subsequence is "ace" and its length is 3.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    
#         ##recursion (time limit exceeded)
        
#         if len(text1)==0 or len(text2)==0:
#             return 0
#         if text1[-1]==text2[-1]:
#             return 1+self.longestCommonSubsequence(text1[:-1], text2[:-1])
#         else:
#             return max(self.longestCommonSubsequence(text1[:-1], text2), 
#                       self.longestCommonSubsequence(text1, text2[:-1]))
        
        ##dp (this is a very good questions, explained here: https://www.youtube.com/watch?v=ASoaQq66foQ)
        ## O(n**2)
        dp= [[0]*(len(text1)+1) for _ in range(len(text2)+1)]
        for i in range(1,len(text2)+1):
            for k in range(1, len(text1)+1):
                if text1[k-1]==text2[i-1]:
                    dp[i][k]= 1+ dp[i-1][k-1]
                else:
                    dp[i][k]=max(dp[i-1][k], dp[i][k-1])
        //print(dp)
        return dp[len(text2)][len(text1)]
        
                