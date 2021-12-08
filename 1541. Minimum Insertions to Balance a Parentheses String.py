# 1541. Minimum Insertions to Balance a Parentheses String
# Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:
#
# Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
# Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
# In other words, we treat '(' as openning parenthesis and '))' as closing parenthesis.
#
# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
#
# You can insert the characters '(' and ')' at any position of the string to balance it if needed.
#
# Return the minimum number of insertions needed to make s balanced.

class Solution:
    def minInsertions(self, s: str) -> int:
        """
        when s[i] = '(':
            need += 2; if need is odd: res += 1 and need -= 1
        else:
            need -= 1; if need < 0: res += 1 and need = 1
        """
        out, need = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                need += 2
                if need % 2:
                    out += 1
                    need -= 1
            else:
                need -= 1
                if need < 0:
                    out += 1
                    need = 1
        return out + need
