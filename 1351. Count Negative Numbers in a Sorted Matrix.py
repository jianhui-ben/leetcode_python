#Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

#Return the number of negative numbers in grid.

 

#Example 1:

#Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#Output: 8
#Explanation: There are 8 negatives number in the matrix.
#Example 2:

#Input: grid = [[3,2],[1,0]]
#Output: 0
#Example 3:

#Input: grid = [[1,-1],[-1,-1]]
#Output: 3
#Example 4:

#Input: grid = [[-1]]
#Output: 1

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n_value= len(grid[0])
        neg_list=[]
        n=0
        for i, x in enumerate(grid):
            k=0
            try:
                while k<= n_value and x[k]>=0:
                    k+=1
            except: 
                k= n_value
            neg_list.append(k)
        for x in neg_list:
            n+= (n_value-x)
        return n
                