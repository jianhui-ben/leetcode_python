#32. Longest Valid Parentheses
#Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

#Example 1:

#Input: s = "(()"
#Output: 2
#Explanation: The longest valid parentheses substring is "()".

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        two pointer + two pass (left to right, right to left)
        
        ) ( ) ( ( ) ) )
        
        ( ( ( )
        
        open: 3
        close: 1
        res: 0 
        
        """
            
        res = 0
        open_brackets, close_brackets = 0, 0

        for i in s:
            if i == '(':
                open_brackets += 1
            else:
                close_brackets += 1

            if open_brackets == close_brackets:
                res = max(res, open_brackets + close_brackets)
            elif close_brackets > open_brackets:
                open_brackets, close_brackets = 0, 0

        open_brackets, close_brackets = 0, 0

        for i in s[::-1]:
            if i == '(':
                open_brackets += 1
            else:
                close_brackets += 1

            if open_brackets == close_brackets:
                res = max(res, open_brackets + close_brackets)
            elif close_brackets < open_brackets:
                open_brackets, close_brackets = 0, 0                   
                    
                    
        return res
                
                
        
        
        
        
        
        
        
        
        
        """
        dp method:
        dp[i]: lenght of longest Valid Parentheses ending in s[i]
        if s[i-1] == '(', then dp[i] = 0
        else:
        if s[i] == '(', then dp[i] == dp[i-2] + 2
        if s[i- dp[i-1] -1] == '(', then dp[i] = 2+ dp[i-1] + dp[i- dp[i-1] -2]
        
        
            (    (XXXX ) )
                   i                 
        """
        if not s: return 0
        dp = [0 for _ in range(len(s))]
        
        for i in range(len(dp)):
            
            if s[i] == '(':
                continue
            
            elif s[i] == ')' and i>=1 and s[i-1] == '(':
                if i >= 2:
                    dp[i] = dp[i-2] +2
                else:
                    dp[i] = 2
            
            elif i >= 1 and i- dp[i-1] -1 >= 0 and s[i- dp[i-1] -1] == '(':
                if i- dp[i-1] -2 >= 0:
                    dp[i] = 2+ dp[i-1] + dp[i- dp[i-1] -2]
                else:
                    dp[i] = 2+ dp[i-1] 
        return max(dp)
            
            
            
        
        
        
        
        
        
#         """
#         stack
#         ) ( ) ( ) )
#         ^
        
#         stack [0, 3, 4]
#         res: 2 - 0 = 2
#         res: 4 - 0 =4
        
        
        
#         """ 
        
#         stack = [-1]
#         res = 0
        
#         for i, ch in enumerate(s):
#             if ch == '(':
#                 stack.append(i)
#             elif ch == ')':
#                 start_idx = stack.pop()
#                 if not stack:
#                     stack.append(i)
#                 else:
#                     res = max(res, i - stack[-1])
                    
#         return res                
        