#850. Rectangle Area II
#We are given a list of (axis-aligned) rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] , where (xi1, yi1) are the coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner of the ith rectangle.

#Find the total area covered by all rectangles in the plane. Since the answer may be too large, return it modulo 109 + 7.

 

#Example 1:


#Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
#Output: 6
#Explanation: As illustrated in the picture.

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        
        ## very hard question
        """
        from left to right
        use active (list) to store the active intervals
        
        for (0, 0, 2, 2)--> add(0, 2) into active intervals to x = 0
                        --> remove(0, 2) form active intervals when x = 2
        """
        
        events = []
        
        add_, remove_ = 0, 1
        for x1, y1, x2, y2 in rectangles:
            events.append((x1, add_, y1, y2))
            events.append((x2, remove_, y1, y2))
        
        events.sort()
        
        cur_x = events[0][0]
        active, ans = [], 0
        
        def mergeIntervals(active):
            res = 0
            cur_y = 0
            
            for y1, y2 in active:
                cur_y = max(cur_y, y1)
                res += max(y2 - cur_y, 0)
                cur_y = max(y2, cur_y)
            return res
        
        # active = [(0, 2), (1, 4), (6, 8)]
        # print(mergeIntervals(active))
        # active = []
        
        
        for x, type_, y1, y2 in events:
            ans += (x - cur_x) * mergeIntervals(active)
            
            if type_ == 0:
                active.append((y1, y2))
                active.sort()
            else:
                active.remove((y1, y2))
                
            cur_x = max(x, cur_x)
            
        return ans % (10**9 + 7)
            
        
        
        
        
        
        
        
        
        
        
        