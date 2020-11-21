#Meeting Rooms (Leetcode Premium)

#Given an array of meeting time intervals consisting of 
#start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a 
#person could attend all meetings.

#(0,8),(8,10) is not conflict at 8

#Have you met this question in a real interview?  
#Example
#Example1

#Input: intervals = [(0,30),(5,10),(15,20)]
#Output: false
#Explanation: 
#(0,30), (5,10) and (0,30),(15,20) will conflict


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
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        if not intervals: return True
        intervals.sort(key= lambda item: item.start)
        upper=intervals[0].end
        for i in intervals[1:]:
            if i.start< upper:
                return False
            else:
                upper= i.end
        return True