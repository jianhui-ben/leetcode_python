#161. One Edit Distance
#Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

#A string s is said to be one distance apart from a string t if you can:

#Insert exactly one character into s to get t.
#Delete exactly one character from s to get t.
#Replace exactly one character of s with a different character to get t.
 

#Example 1:

#Input: s = "ab", t = "acb"
#Output: true
#Explanation: We can insert 'c' into s to get t.
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        
        if abs(len(s) - len(t)) > 1:
            return False
        if len(s) >= len(t):
            short, long = t, s
        else:
            short, long = s, t
            
        off, short_i, long_i = 0, 0, 0
        
        while short_i < len(short):
            if long[long_i] == short[short_i]:
                long_i += 1
                short_i += 1
            
            elif len(long) > len(short):
                long_i += 1
                off += 1
            else:
                long_i += 1
                short_i += 1
                off += 1
            
            if off > 1:
                break
        if off:
            return off == 1
        return off + len(long) - len(short) == 1
        
        