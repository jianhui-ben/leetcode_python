#85. Maximal Rectangle
#Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        go top down
        dp[i][j] = how many consecutive 1s from matrix[0][j] to matrix[i][j]
        
        for example:
        dp[1]: [2, 0, 2, 1, 1]
        dp[2]: [3, 1, 3, 2, 2]
        dp[3]: [4, 0, 0, 3, 0]
        
        how we find the max rectangles in each dp histogram: leet 84
        """
        if not matrix: return 0
        dp = [0 for _ in range(len(matrix[0]))]
        cur_row, out = 0, 0 
        
        def largestRecHistogram(heights):
            stack, out = [], 0
            for i, height in enumerate(heights):
                while stack and heights[stack[-1]] > height:
                    cur_height = heights[stack.pop()]
                    if stack:
                        cur_width = i - (stack[-1] + 1)
                    else:
                        cur_width = i
                    out = max(out, cur_width * cur_height)
                stack.append(i)
            i = len(heights)
            while stack:
                cur_height = heights[stack.pop()]
                if stack:
                    cur_width = i - (stack[-1] + 1)
                else:
                    cur_width = i
                out = max(out, cur_width * cur_height)  
            return out
                
        while cur_row < len(matrix):
            for i in range(len(dp)):
                if matrix[cur_row][i] == '1':
                    dp[i] += 1
                else:
                    dp[i] = 0
            # print(dp)
            out = max(out, largestRecHistogram(dp))
            cur_row += 1

        return out
            
        