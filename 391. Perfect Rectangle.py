#391. Perfect Rectangle
#Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned rectangle. The bottom-left point of the rectangle is (xi, yi) and the top-right point of it is (ai, bi).

#Return true if all the rectangles together form an exact cover of a rectangular region.
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        ## O(n), O(n)
        ## math way:
        ##  [[1,1,3,3],
        ##   [3,1,4,2],
        ##   [3,2,4,4],
        ##   [1,3,2,4],
        ##   [2,3,3,4]]

        ## we compare the area and # of angles
        ## first area:
        cur_area = 0
        x, y, a, b = float('inf'), float('inf'), float('-inf'), float('-inf')
        ## angles
        stored_angles =set()
        
        for xi, yi, ai, bi in rectangles:
            x = min(xi, x)
            y = min(yi, y)
            a = max(ai, a)
            b = max(bi, b)
            cur_area += (ai-xi) * (bi-yi)
            
            if (xi, yi) not in stored_angles:
                stored_angles.add((xi, yi))
            else:
                stored_angles.remove((xi, yi))
            if (xi, bi) not in stored_angles:
                stored_angles.add((xi, bi))
            else:
                stored_angles.remove((xi, bi))
            if (ai, bi) not in stored_angles:
                stored_angles.add((ai, bi))
            else:
                stored_angles.remove((ai, bi))
            if (ai, yi) not in stored_angles:
                stored_angles.add((ai, yi))
            else:
                stored_angles.remove((ai, yi))
            
            
        if (a-x) * (b-y)!= cur_area: return False
        if len(stored_angles)!=4: return False
        if (x, y) not in stored_angles or (x, b) not in stored_angles \
        or (a, b) not in stored_angles or (a, y) not in stored_angles:
            return False
        return True
                
            
            
            
        