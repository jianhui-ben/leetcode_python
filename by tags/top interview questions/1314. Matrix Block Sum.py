#1314. Matrix Block Sum
#Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.
 

#Example 1:

#Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
#Output: [[12,21,16],[27,45,33],[24,39,28]]


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        ##brute force compression horizontally and vertically
        if K==0: return mat
        out1=[]
        
        def sliding_sum(row, k):
            dp=[None]* len(row)
            dp[0]= sum(row[: min(k+1, len(row))])
            for i in range(1, len(row)):
                minus, plus=0, 0
                if i-k>0:
                    minus=row[i-k-1]
                if i+k<len(row):
                    plus=row[i+k]
                dp[i]=dp[i-1]-minus+plus
            return dp
        
        for row in mat:
            out1.append(sliding_sum(row, K))
        # print(out1)
        ## do sliding sum vertically
        out1=  [[row[k] for row in out1] for k in range(len(out1[0]))]
        out2=[]
        for row in out1:
            out2.append(sliding_sum(row, K))
        
        ##transpose out2
        return [[row[k] for row in out2] for k in range(len(out2[0]))]