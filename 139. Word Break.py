#139. Word Break

#Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
#determine if s can be segmented into a space-separated sequence of one or more dictionary words.

#Note:

#The same word in the dictionary may be reused multiple times in the segmentation.
#You may assume the dictionary does not contain duplicate words.
#Example 1:

#Input: s = "leetcode", wordDict = ["leet", "code"]
#Output: true
#Explanation: Return true because "leetcode" can be segmented as "leet code".


## burtal force: n**n
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict: return True
        for i in range(len(s)-1, -1,-1):
            if s[i:] in wordDict and self.wordBreak(s[:i],wordDict):
                return True
        return False


##dp:
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    
        # dp
        dp=[[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            for k in range(i, -1, -1):
                if s[k:i+1] in wordDict: 
                    dp[k][i]=True
                else:
                    for m in range(k, i):
                        if dp[k][m]==True and dp[m+1][i]==True:
                            dp[k][i]=True
                            break
        return dp[0][-1]