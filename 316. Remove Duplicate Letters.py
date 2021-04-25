#316. Remove Duplicate Letters
#Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

#Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

 

#Example 1:

#Input: s = "bcabc"
#Output: "abc"
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ## greedy method
        ## O(n), O(1) space due to stack can have 26 in max
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
            
            
        