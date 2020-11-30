#844. Backspace String Compare
#Given two strings S and T, return if they are equal when both 
#are typed into empty text editors. # means a backspace character.

#Note that after backspacing an empty text, the text will continue empty.

#Example 1:

#Input: S = "ab#c", T = "ad#c"
#Output: true
#Explanation: Both S and T become "ac".


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        ##brute force:
        def convert(s):
            if not s: return None
            new_s= ""
            for c in s:
                if c!= '#':
                    new_s+=c
                if c=='#' and new_s!="":
                    new_s=new_s[:-1]
            return new_s
        return convert(S)==convert(T)