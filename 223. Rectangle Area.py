#223. Rectangle Area
#Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

#The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

#The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

# https://leetcode.com/problems/rectangle-area/

#Example 1:

#Rectangle Area
#Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
#Output: 45

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        """
        check if these two have overlaps
        
        ax2 > bx1 and ax1 < bx2 --> overlaps
        
        max(ax1, bx1), max(ay1, by1), min(ax2, bx2), min(ay2, by2)
        """
        
        def getArea(x1, y1, x2, y2):
            if x1 >= x2 or y1 >= y2:
                return 0
            
            return (x2-x1) * (y2-y1)
        
        two_rec_sum = getArea(ax1, ay1, ax2, ay2) + getArea(bx1, by1, bx2, by2) 
        if ax2 > bx1 and ax1 < bx2:
            return two_rec_sum - getArea(max(ax1, bx1), max(ay1, by1), min(ax2, bx2), min(ay2, by2))
        return two_rec_sum