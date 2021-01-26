#115. Distinct Subsequences
#Given two strings s and t, return the number of distinct subsequences of s which equals t.

#A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

#It's guaranteed the answer fits on a 32-bit signed integer.

 

#Example 1:

#Input: s = "rabbbit", t = "rabbit"
#Output: 3
#Explanation:
#As shown below, there are 3 ways you can generate "rabbit" from S.
#rabbbit
#rabbbit
#rabbbit


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ## iterative dynamic programming:
        
        
        
        ## recursion with mem
        ## time O(M* N), space O(M*N)
        self.mem= {}
        return self.dfs(s, t, 0, 0)

    
    def dfs(self, s,t,i, j):
        if j== len(t):
            return 1
        elif i==len(s):
            return 0
        elif (i, j) in self.mem:
            return self.mem[(i, j)]
        if s[i]!= t[j]:
            k= self.dfs(s,t,i+1, j)
            self.mem[(i, j)]=k
            return k
        elif s[i]==t[j]:
            k= self.dfs(s,t,i+1, j)+ self.dfs(s,t,i+1, j+1)
            self.mem[(i, j)]=k
            return k    

        
        
#         ##brute force: dfs: 2**N
#         self.out=0
#         self.dfs(s, t, 0, "")
#         return self.out
    
#     def dfs(self, s, t, idx, cur):
#         if cur==t:
#             self.out+=1
#             return
#         if idx< len(s):
#             if s[idx]== t[len(cur)]:
#                 self.dfs(s, t, idx+1, cur+s[idx])
#             self.dfs(s, t, idx+1, cur)

                
            
        
        