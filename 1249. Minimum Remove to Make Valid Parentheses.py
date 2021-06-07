#1249. Minimum Remove to Make Valid Parentheses
#Given a string s of '(' , ')' and lowercase English characters. 

#Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

#Formally, a parentheses string is valid if and only if:

#It is the empty string, contains only lowercase characters, or
#It can be written as AB (A concatenated with B), where A and B are valid strings, or
#It can be written as (A), where A is a valid string.
 

#Example 1:

#Input: s = "lee(t(c)o)de)"
#Output: "lee(t(c)o)de"


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ##stack
        stack = []
        for i in range(len(s)):
            if s[i]!='(' and s[i]!=')':
                continue
            elif s[i]=='(':
                stack.append(i)
            elif s[i]==')' and stack and s[stack[-1]]=='(':
                stack.pop()
            elif s[i]==')':
                stack.append(i)
        stack=set(stack)
        return ''.join([s[i] for i in range(len(s)) if i not in stack])
        