#84. Largest Rectangle in Histogram
#Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

#Example 1:


#Input: heights = [2,1,5,6,2,3]
#Output: 10
#Explanation: The above is a histogram where width of each bar is 1.
#The largest rectangle is shown in the red area, which has an area = 10 units.

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        stack method
        keep non-descending heights in the stacks
        O(n) solution
        
        2, 1, 5, 6, 2, 3
        
        rectangle = height * width
        stack = [(1, 1), (2, 5), (3, 6)]    ## (index, height)
        we see (4, 2)
        rectangles: height: 6; width: 4 - (2+1), pop out(3, 6)
                    height: 5; width: 4 - (1+1), pop out(2, 5)
        
        stack: [(1, 1), (4, 2), (5, 3)]
        rectangles: height: 3; width: 6 -(4+1), pop out(5, 3)
                    height: 2; width: 6 -(1+1), pop out (4, 2)
                    height: 1; width: 6
                    
        2, 3, 1
        [(0, 2), (1, 3)]
        we got (2, 1)
        rectangles: height: 3; width: 2 -(0+1), pop out(1, 3)
                    height: 2; width: 2, pop out(0, 2)
        [(2, 1)]
        rectangles: height: 1; width: 3, pop out(5, 3)
        """
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
        
        
        
        
        
        
#         stack = []
#         out = 0
#         heights = [0] + heights + [0]
#         for i, height in enumerate(heights):

#             while stack and height < heights[stack[-1]]:
#                 cur_i = stack.pop()
#                 cur_height = heights[cur_i]
#                 if stack:
#                     width = i - stack[-1] -1
#                 else:
#                     width = i - 1
#                 out = max(out, width * cur_height)
#             stack.append(i)
        
#         ## [1, 1]
#         # i = len(heights)
#         # while stack:
#         #     cur_i = stack.pop()
#         #     cur_height = heights[cur_i]
#         #     if stack:
#         #         width = i - stack[-1] -1
#         #     else:
#         #         width = i - 1
#         #     out = max(out, width * cur_height)
#         return out
            

                
                    
        
        
        
        
        
        
        
        """
        divide and conquer
        O(n log n) best case, worst case O(n**2)
        """
#         if not heights: return 0
#         min_index = 0
#         for i in range(len(heights)):
#             if heights[i] < heights[min_index]:
#                 min_index = i
                
#         return max(
#             self.largestRectangleArea(heights[:min_index]),
#             self.largestRectangleArea(heights[min_index+1: ]),
#             len(heights) * heights[min_index]
#         )
        
        
        
        
        
        
        
        
        
        
        """
        brute force: O(n**2)
        get pair of (i, j) where 0<= i<=j<len(heights)
        get the area in heights[i:j+1]
        """
        
        # out = 0
        # for i in range(len(heights)):
        #     cur_height = heights[i]
        #     for j in range(i, len(heights)):
        #         cur_height = min(cur_height, heights[j])
        #         out = max(out, cur_height * (j-i + 1))
        # return out


