#32. Longest Valid Parentheses
#Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

#Example 1:

#Input: s = "(()"
#Output: 2
#Explanation: The longest valid parentheses substring is "()".


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        stack
        """ 
        
        stack = [-1]
        res = 0
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                start_idx = stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
                    
        return res                
        