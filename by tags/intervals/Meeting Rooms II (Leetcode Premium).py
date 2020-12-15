#Meeting Rooms II (Leetcode Premium)
#Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] 
#(si < ei), find the minimum number of conference rooms required.

#Example1

#Input: intervals = [(0,30),(5,10),(15,20)]
#Output: 2
#Explanation:
#We need two meeting rooms
#room1: (0,30)
#room2: (5,10),(15,20)

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        if not intervals: return 0
        intervals.sort(key=lambda item: item.start)
        out= [intervals[0].end]
        for i in intervals[1:]:
            if i.start<out[0]:
                out.append(i.end)
            else:
                out[0]= i.end
            out.sort()
        return len(out)
