#221. Maximal Square


#Given an m x n binary matrix filled with 0's and 1's, 
#find the largest square containing only 1's and return its area.

 

#Example 1:


#Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],
#                 ["1","1","1","1","1"],["1","0","0","1","0"]]
#Output: 4
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ##dp:
        if not matrix: return 0
        dp=matrix.copy()
        out=0
        if "1" in dp[0] or "1" in [m[0] for m in dp]:
            out+=1
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if dp[r][c]=='1':
                    dp[r][c]= min(int(dp[r-1][c-1]), \
                                  int(dp[r-1][c]), \
                                  int(dp[r][c-1]))+1
                    print(dp[r][c])
                    out=max(out, dp[r][c])
                    
        return out*out
        
       
#         ##brute force
#         if not matrix: return 0
#         self.out=0
        
#         def dfs(matrix, r, c, i):
#             self.out= max(self.out, i**2)
#             if r+i<len(matrix) and c+i < len(matrix[0]):
#                 for a in range(r, r+i+1):
#                     for b in range(c, c+i+1):
#                         if matrix[a][b]!='1':
#                             return
#                 dfs(matrix, r, c, i+1)

#         for r in range(len(matrix)):
#             for c in range(len(matrix[0])):
#                 if matrix[r][c]=='1':
#                     dfs(matrix, r, c, 1)

#         return self.out
            

            
            
            
        
        