#Given an integer matrix, find the length of the longest increasing path.

#From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

#Example 1:

#Input: nums = 
#[
#  [9,9,4],
#  [6,6,8],
#  [2,1,1]
#] 
#Output: 4 
#Explanation: The longest increasing path is [1, 2, 6, 9].

##method 1: depth-first search with recursions
class Solution(object):    
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix)==0: return 0
        
        
        def dfs(x,y):
            for dx, dy in zip([1,0, -1, 0], [0, 1, 0, -1]):
                nx, ny= x+dx, y+dy
                if 0<=nx<r_tot and 0<=ny<c_tot and matrix[nx][ny]> matrix[x][y]:
                    if dps[nx][ny]==0: dps[nx][ny]=dfs(nx,ny)
                    dps[x][y]= max(dps[x][y], dps[nx][ny]+1)
            dps[x][y]= max(dps[x][y], 1)
            return dps[x][y]

        
        r_tot, c_tot= len(matrix), len(matrix[0])
        dps=[[0] * c_tot for x in range(r_tot)]
        # dps=list([[0]* c_tot]*r_tot)  #still don't understand why this is wrong
        for r in range(r_tot):
            for c in range(c_tot):
                if dps[r][c]==0:
                    dps[r][c]= dfs(r, c)
        return max([max(x) for x in dps])

