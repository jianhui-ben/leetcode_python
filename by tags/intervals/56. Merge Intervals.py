#56. Merge Intervals
#Given an array of intervals where intervals[i] = [starti, endi], merge all 
#overlapping intervals, and return an array of the non-overlapping intervals that 
#cover all the intervals in the input.

 

#Example 1:

#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].


##time O(n); space O(1)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ## iterative method
        ##sort
        ##for inter in intervals: create cur_inter, expand the upper bound if the next head is
        ## below the upper bound until the next head is bigger than the upper bound
        if not intervals: return []
        out=[]
        intervals.sort(key=lambda item:item[0])
        # print(intervals)
        lower, upper=intervals[0]
        for head, tail in intervals[1:]:
            if head<= upper:
                upper= max(tail, upper)
            else: 
                out.append([lower, upper])
                lower, upper=head, tail
        out.append([lower, upper])
        return out
        
            
        
        
        
        
