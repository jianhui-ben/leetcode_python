#Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

#If there isn't any rectangle, return 0.

 

#Example 1:

#Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
#Output: 4


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # method 2: check the right_most edge
        from collections import defaultdict 
        stored=defaultdict(list)
        for x, y in points:
            stored[x].append(y)
        
        lastx= {}
        out= float('inf')
        for x, ys in sorted(stored.items()):
            ys.sort()
            for k, y2 in enumerate(ys):
                for i in range(k):
                    y1= ys[i]
                    if (y1, y2) in lastx:
                        out=min(out, abs(y1-y2)*abs(lastx[y1,y2]- x))
                    lastx[y1,y2]= x
                    
        return out if out<float('inf') else 0
                        
            
#         ##brute force: diagonal
#         ## if we find two points (x1, y1) and (x2, y2)
#         ## there're also (x1, y2), (X2, y1) in the points
#         ## then the rectangle exists
        
#         ## first store all the points into hashtable
        
#         if len(points)<4: return 0

#         points.sort()
#         from collections import defaultdict 
#         stored=defaultdict(list)
#         for x, y in points:
#             stored[x].append(y)
#         out=float('inf')
#         rects=[]
#         for i in range(len(points)-1):
#             x1, y1= points[i]
#             for k in range(i+1, len(points)):
#                 cur_out=float('inf')
#                 x2, y2=points[k]
#                 if x1!=x2 and y1!=y2 and y2 in stored[x1] and y1 in stored[x2]:
#                     out= min(out, abs(x2-x1)* abs(y2-y1))
#         if out==float('inf'):return 0
#         else: return out
        
        
    
