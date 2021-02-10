#973. K Closest Points to Origin

#We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

#(Here, the distance between two points on a plane is the Euclidean distance.)

#You may return the answer in any order.  The answer is guaranteed to be unique 
#(except for the order that it is in.)

 

#Example 1:

#Input: points = [[1,3],[-2,2]], K = 1
#Output: [[-2,2]]
#Explanation: 
#The distance between (1, 3) and the origin is sqrt(10).
#The distance between (-2, 2) and the origin is sqrt(8).
#Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
#We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].



class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        maxheap=[]
        for x, y in points:
            maxheap.append((x**2+y**2, (x, y)))
        maxheap.sort(key=lambda item:item[0])
        if K >len(maxheap): return None
        else: return [list(value) for dis, value in maxheap[:K]]