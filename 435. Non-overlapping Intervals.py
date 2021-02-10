#435. Non-overlapping Intervals
#Given a collection of intervals, find the minimum number of intervals you 
#need to remove to make the rest of the intervals non-overlapping.

 

#Example 1:

#Input: [[1,2],[2,3],[3,4],[1,3]]
#Output: 1
#Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ##brute force
        if not intervals or len(intervals)==1: return 0
        intervals.sort(key= lambda item: item[0])
        count=0
        upper= intervals[0][1]
        for head, tail in intervals[1:]:
            if head>=upper:
                upper= tail
            else:
                count+=1
                upper=min(tail, upper)
        return count
            