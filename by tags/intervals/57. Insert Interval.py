#57. Insert Interval
#Given a set of non-overlapping intervals, insert a new interval into the intervals 
#(merge if necessary).

#You may assume that the intervals were initially sorted according to their start times.

 

#Example 1:

#Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
#Output: [[1,5],[6,9]]
#Example 2:

#Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
#Output: [[1,2],[3,10],[12,16]]
#Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        new_start, new_end= newInterval
        head, tail=intervals[0][0], intervals[-1][1]
        i1, i2=0, 0
        if new_start>tail:
            intervals.append(newInterval)
            return intervals
        else:
            for i, inter in enumerate(intervals):
                if new_start<=inter[0]:
                    if i==0:
                        i1= 0
                    elif new_start>intervals[i-1][1] :
                        i1= i
                    else:
                        i1=i-1
                    break
                i1=i
        if new_end<head:
            intervals.insert(0,newInterval)
            return intervals
        else:
            for i in range(len(intervals)-1, -1, -1):
                if new_end>= intervals[i][1]:
                    if i==len(intervals)-1:
                        i2= len(intervals)-1
                    elif new_end<intervals[i+1][0]:
                        i2=i
                    else:
                        i2= i+1
                    break
                i2=i
        # print(i1, i2)
        ans=[inter for i, inter in enumerate(intervals) if i<i1 or i>i2]
        ans.append([min(intervals[i1][0], new_start), max(new_end, intervals[i2][1])])
        return sorted(ans, key= lambda item: item[0])
