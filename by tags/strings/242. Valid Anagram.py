#242. Valid Anagram
#Given two strings s and t , write a function to determine if t is an anagram of s.

#Example 1:

#Input: s = "anagram", t = "nagaram"
#Output: true
#Example 2:

#Input: s = "rat", t = "car"
#Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ##hash table
        if len(s)!=len(t): return False
        stored= {}
        for i in s:
            if i in stored:
                stored[i]+=1
            else: stored[i]=1
        for k in t:
            if k not in stored or stored[k]<1:
                return False
            else: stored[k]-=1
        return True
