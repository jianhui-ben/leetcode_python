#290. Word Pattern

#Given a pattern and a string s, find if s follows the same pattern.

#Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

#Example 1:

#Input: pattern = "abba", s = "dog cat cat dog"
#Output: true


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ## two hashtables
        stored_p, stored_w= dict(), dict()
        l_words= s.split()
        if len(l_words)!=len(pattern): return False
        for i in range(len(pattern)):
            if pattern[i] in stored_p and l_words[i]!=stored_p[pattern[i]]:
                return False
            if l_words[i] in stored_w and pattern[i]!= stored_w[l_words[i]]:
                return False
            stored_p[pattern[i]]=l_words[i]
            stored_w[l_words[i]]= pattern[i]
        return True
            