#759. Employee Free Time
#We are given a list schedule of employees, which represents the working time for each employee.

#Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

#Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

#(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

 

#Example 1:

#Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
#Output: [[3,4]]
#Explanation: There are a total of three employees, and all common
#free time intervals would be [-inf, 1], [3, 4], [10, inf].
#We discard any intervals that contain inf as they aren't finite.
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        """
        monotone stack
        
        [2, 3], [5, 6]
          ^
        [1.4 , 3], [4, 10]
         ^
        [1.2, 1.7]
        ^
        
        ascending stack by start time
        
        (4, 10), (5, 6), (7, 8)
        (4, 10)
        
        keep a minheap of starting time
        heappop the min_start time, end_time
        continue to heappop unil heap[0].start_time > end_time
        """
        out, heap = [], []
                
        for worker_id, intervals in enumerate(schedule):
            heapq.heappush(heap, (intervals[0].start, -intervals[0].end, worker_id, 0))
            
        while heap:
            
            cur_start, cur_end, cur_worker, cur_worker_pointer = heapq.heappop(heap)
            cur_end = -cur_end
            
            if cur_worker_pointer + 1 < len(schedule[cur_worker]):
                heapq.heappush(heap, \
                               (schedule[cur_worker][cur_worker_pointer + 1].start,
                                -schedule[cur_worker][cur_worker_pointer + 1].end,
                                 cur_worker, cur_worker_pointer + 1))
            
            while heap and heap[0][0] <= cur_end:
                _, new_end, pop_worker, pop_worker_pointer = heapq.heappop(heap)
                cur_end = max(cur_end, - new_end)
                if pop_worker_pointer + 1 < len(schedule[pop_worker]):
                    heapq.heappush(heap, \
                                   (schedule[pop_worker][pop_worker_pointer + 1].start,
                                    -schedule[pop_worker][pop_worker_pointer + 1].end,
                                     pop_worker, pop_worker_pointer + 1))
            
            if heap:
                out.append(Interval(start = cur_end, end = heap[0][0]))
            

        # print([len(i) for i in schedule])
        
        """
        [1, 3], [6, 7]
        [2, 4]
        [2, 5], [9, 12]
        
        heap: 
        [1, 3], [2, 4], [2, 5]
        
        [2, 5], [2, 4], [1, 3]
        
        """
        
        return out
            
            
            
        