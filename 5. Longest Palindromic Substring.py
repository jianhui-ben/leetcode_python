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
    def longestPalindrome(self, s: str) -> str:
        ## here two pointer would be better than dp
        ## O(n**2), O(1)
        res=''
        def checkPalindrome(s, l, r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1: r]
        
        
        for i in range(len(s)):
            res1 = checkPalindrome(s, i, i)
            if i+1<len(s) and s[i]==s[i+1]:
                res2 = checkPalindrome(s, i, i+1)
            else: res2= ''
            if len(res1)>= len(res2) and len(res1)>len(res):
                res = res1
            elif len(res2)>= len(res1) and len(res2)>len(res):
                res = res2
        return res
        

        
        ## dp: TLE
        ## status: dp[i][j]=True if s[i:j+1] is Palindromic , j>=i
        ## base: i==j: dp[i][j]=True
        ## 
        ## if i+1>j-1: dp[i][j] =s[i]==s[j]
        ## else: dp[i][j] = dp[i+1][j-1] and s[i]==s[j]
        
        ## 'bacab'
        ## backward traverse
        res=(0, 0)
        dp = [[None for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(dp)-1, -1, -1):
            for j in range(i, len(dp)):
                if i==j:
                    dp[i][j] = True
                elif i+1>j-1:
                    dp[i][j] =s[i]==s[j]
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i]==s[j]
                if dp[i][j] and j-i>res[1]-res[0]:
                    res= (i, j)
        return s[res[0]: res[1]+1]