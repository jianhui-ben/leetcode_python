#583. Delete Operation for Two Strings

#Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

#In one step, you can delete exactly one character in either string.

 

#Example 1:

#Input: word1 = "sea", word2 = "eat"
#Output: 2
#Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ## similar to find subsequence
        ## use dp, dp[i][j] = the minDis for word1[:i] and word2[:j] where 0<=i<=len(word1)
        ## status change:

        ###   E A T
        ##  0 1 2 3
        ##S 1 2 3 4
        ##E 2 1 2 3
        ##A 3 2 1 2
        
        
        
        ## time O(MN), space O(MN)
        dp=[[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i==0:
                    dp[i][j]=j
                elif j==0:
                    dp[i][j]=i  
                elif word1[i-1]==word2[j-1]:
                    dp[i][j]= dp[i-1][j-1]
                else:
                    dp[i][j] = 1+ min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
                    