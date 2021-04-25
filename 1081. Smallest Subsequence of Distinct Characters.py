#1081. Smallest Subsequence of Distinct Characters
#Return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

#Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/

 

#Example 1:

#Input: s = "bcabc"
#Output: "abc"

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        ## greedy method
        stored = dict(Counter(s))
        if len(s)==1: return s
        stack = [s[0]]
        stored[s[0]]-=1
        for i in range(1, len(s)):
            if s[i] not in stack:
                while stack and s[i]<stack[-1] and stored[stack[-1]]>0:
                    stack.pop()
                stack.append(s[i])
            stored[s[i]]-=1
        
        return ''.join(stack)
            
                
        
        
        
        