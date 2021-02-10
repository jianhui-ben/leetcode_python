#291. Word Pattern II
#Given a pattern and a string s, return true if s matches the pattern.

#A string s matches a pattern if there is some bijective mapping of single characters to strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.

 

#Example 1:

#Input: pattern = "abab", s = "redblueredblue"
#Output: true
#Explanation: One possible mapping is as follows:
#'a' -> "red"
#'b' -> "blue"


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        ##dfs + backtracking
        stored_p, stored_w= {}, {}
        return self.dfs(pattern, s, stored_p, stored_w)
    
    
    def dfs(self, pattern, s, stored_p, stored_w):
        if not pattern:
            return len(s)==0
        if pattern[0] in stored_p:
            exist_word= stored_p[pattern[0]]
            if len(s)<len(exist_word) or s[:len(exist_word)]!=exist_word:
                return False
            else:
                return self.dfs(pattern[1:], s[len(exist_word):], stored_p, stored_w)
        
        for i in range(len(s)):
            word=s[:i+1]
            cur_p=pattern[0]
            if word in stored_w: continue
            stored_p[cur_p]= word
            stored_w[word]= cur_p
            if self.dfs(pattern[1:], s[i+1:], stored_p, stored_w): return True
            stored_p.pop(cur_p)
            stored_w.pop(word)
        return False