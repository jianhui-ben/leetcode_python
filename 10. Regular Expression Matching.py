#10. Regular Expression Matching
#Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

#'.' Matches any single character.​​​​
#'*' Matches zero or more of the preceding element.
#The matching should cover the entire input string (not partial).
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ##dp
        ## dp[i][j] =True/False: s[:i+1] and p[:j+1]
        ## choice: for '*', we could choose its previous chara to repeat any times \
        ## until its index reach len(s)
        ## O(len(s)* len(p))
        
        self.mem=defaultdict()
        def recursion(s, p, i, j):
            if j==len(p): return i==len(s)
            if (i, j) in self.mem: return self.mem[(i, j)]
            first = i<len(s) and (s[i]==p[j] or p[j]=='.')
            if j+1<len(p) and p[j+1]=='*':
                res= recursion(s, p, i, j+2) or \
                    (first and recursion(s, p, i+1, j))
            else:
                res= first and recursion(s, p, i+1, j+1)
            self.mem[(i, j)]=res
            return self.mem[(i, j)]

        return recursion(s, p, 0, 0)
        