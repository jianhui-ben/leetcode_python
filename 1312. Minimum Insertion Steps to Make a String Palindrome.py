#1312. Minimum Insertion Steps to Make a String Palindrome
#Given a string s. In one step you can insert any character at any index of the string.

#Return the minimum number of steps to make s palindrome.

#A Palindrome String is one that reads the same backward as well as forward.

 

#Example 1:

#Input: s = "zzazz"
#Output: 0
#Explanation: The string "zzazz" is already palindrome we don't need any insertions.
class Solution:
    def minInsertions(self, s: str) -> int:
        ## dp
        ## dp[i][j]= min steps to make s[i:j+1] Palindrome
        ## base: i==j: dp[i][j]=0
        ## return dp[0][len(s)-1]
        ## if s[i]==s[j]:dp[i][j] = dp[i+1][j-1]
        ## else:dp[i][j] = 1+min(dp[i+1][j], dp[i][j-1])
        
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(dp)-1, -1, -1):
            for j in range(i, len(dp)):
                if i==j:
                    continue
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i+1][j], dp[i][j-1])
                    
        return dp[0][-1]
    
        ## space compression
        dp= [0 for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            temp= [0 for _ in range(len(s))]
            for j in range(i, len(temp)):
                if i==j:
                    continue
                if s[i]==s[j]:
                    temp[j] = dp[j-1]
                else:
                    temp[j] = 1+min(dp[j], temp[j-1])
            dp = temp
                    
        return dp[-1]
        