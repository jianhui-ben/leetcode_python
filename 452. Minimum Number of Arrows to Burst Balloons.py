#452. Minimum Number of Arrows to Burst Balloons
#There are some spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice. The start is always smaller than the end.

#An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.

#Given an array points where points[i] = [xstart, xend], return the minimum number of arrows that must be shot to burst all balloons.


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ## greedy
        ## sort by end ascs
        ## if start<=end: pop
        ## else: update the end, cnt+=1
        ## O(n), O(1)
        if not points: return 0
        points.sort(key = lambda x: x[1])
        cnt, i=0, 0
        compare = float('-inf')
        while i<len(points):
            if points[i][0]>compare:
                cnt+=1
                compare = points[i][1]
            i+=1
        return cnt