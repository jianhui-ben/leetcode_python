#1289. Minimum Falling Path Sum II

#Given a square grid of integers arr, a falling path with non-zero shifts is a choice of exactly one element from each row of arr, such that no two elements chosen in adjacent rows are in the same column.

#Return the minimum sum of a falling path with non-zero shifts.

 

#Example 1:

#Input: arr = [[1,2,3],[4,5,6],[7,8,9]]
#Output: 13
#Explanation: 
#The possible falling paths are:
#[1,5,9], [1,5,7], [1,6,7], [1,6,8],
#[2,4,8], [2,4,9], [2,6,7], [2,6,8],
#[3,4,8], [3,4,9], [3,5,7], [3,5,9]
#The falling path with the smallest sum is [1,5,7], so the answer is 13.

class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        ## dp, sort and just select the top 2
        ## O(N*N*log n), space O(N)
        prev = arr[0]
        for row in range(1, len(arr)):
            prev_min = sorted([(v, i) for i, v in enumerate(prev)])[:2]
            cur = []
            for col in range(len(arr[row])):
                if col!= prev_min[0][1]:
                    cur.append(arr[row][col]+prev_min[0][0])
                else:
                    cur.append(arr[row][col]+prev_min[1][0])
                
            prev = cur
            
        return min(cur)
            
        
        ## dp, go from top to bottom
        ## O(N**3), O(1)
        for row in range(1, len(arr)):
            for col in range(len(arr[row])):
                cur = float('inf')
                for last_col in range(len(arr[row])):
                    if last_col!=col:
                        cur=min(cur, arr[row][col]+ arr[row-1][last_col])
                arr[row][col]=cur
                                
        return min(arr[-1])