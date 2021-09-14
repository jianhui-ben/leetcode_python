#296. Best Meeting Point
#Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

#The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

#The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

 

#Example 1:


#Input: grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
#Output: 6
#Explanation: Given three friends living at (0,0), (0,4), and (2,2).
#The point (0,2) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is minimal.
#So return 6.

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        """
        brute force: O(m*n + m*n + M**2 + n**2)
        """
        horizontal, vertical = [], []
        
        for row in range(len(grid)):
            row_sum = 0
            for col in range(len(grid[0])):
                row_sum += grid[row][col]
            vertical.append(row_sum)
            
        for col in range(len(grid[0])):
            col_sum = 0
            for row in range(len(grid)):
                col_sum += grid[row][col]
            horizontal.append(col_sum)
        
        def get_distance(prefix_sum):
            res = float('inf')
            
            for i in range(len(prefix_sum)):
                cur_sum = 0
                for j in range(len(prefix_sum)):
                    cur_sum += abs(i - j) * prefix_sum[j]
            
                res = min(res, cur_sum)

            return res
            
        
        return get_distance(horizontal) + get_distance(vertical)