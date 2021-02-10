#252. Meeting Rooms
#Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        ##time O(nlog n)
        if not intervals: return True
        intervals.sort(key=lambda x: x[0])
        last_end= intervals[0][0]
        for start, end in intervals:
            if start<last_end:
                return False
            last_end= end
        return True
