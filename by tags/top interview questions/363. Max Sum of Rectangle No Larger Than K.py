#363. Max Sum of Rectangle No Larger Than K
#Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

#Example:

#Input: matrix = [[1,0,1],[0,-2,3]], k = 2
#Output: 2 
#Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
#             and 2 is the max number no larger than k (k = 2).
#Note:

#The rectangle inside the matrix must have an area > 0.
#What if the number of rows is much larger than the number of columns?


class Solution:
    def binary_search(self, l, start, end, target):
        if l[start]>=target: return l[start]
        if l[end]<target: return float("inf") 
        mid= (start+end)//2
        if l[mid]>=target:
            return self.binary_search(l, start, mid, target)
        else:
            return self.binary_search(l, mid+1, end, target)
            
        
        
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix: return None
        row, column= len(matrix), len(matrix[0])
        max_sum=float("-inf")
        for left in range(column):
            for right in range(left, column):
                temp=[None] * row
                for i in range(row):
                    temp[i]= sum(matrix[i][left: right+1])
                
                cum_sum_l=[None]*(len(temp)+1)
                cum_sum_l[0]=0
                cum_sum=0
                for i in range(len(temp)):
                    cum_sum+=temp[i]
                    cum_sum_l[i+1]=cum_sum
                    
                for j in range(1, len(cum_sum_l)):
                    target_value= cum_sum_l[j]-k
                    sub_cum_sum_l=sorted(cum_sum_l[:j])
                    start_value= self.binary_search(sub_cum_sum_l, 0, len(sub_cum_sum_l)-1, target_value)
                    max_sum=max(max_sum, cum_sum_l[j]- start_value)
                    if max_sum==k:
                        return k
        return max_sum