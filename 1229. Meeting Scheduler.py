#1229. Meeting Scheduler
#Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

#If there is no common time slot that satisfies the requirements, return an empty array.

#The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.

#It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

 

#Example 1:

#Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
#Output: [60,68]


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        ## minheap
        ## O(n log n) time, space O(n)
        
        import heapq
        all_slots=[]
        for i in range(max(len(slots1), len(slots2))):
            if i<len(slots1) and slots1[i][1]-slots1[i][0]>=duration:
                heapq.heappush(all_slots, slots1[i])
            if i<len(slots2) and slots2[i][1]-slots2[i][0]>=duration:
                heapq.heappush(all_slots, slots2[i])
        while len(all_slots)>1:
            start1,end1= heapq.heappop(all_slots)
            start2,end2= heapq.heappop(all_slots)
            if start2+duration<=end1:
                return [start2, start2+duration]
            elif end1<=end2:
                heapq.heappush(all_slots, [start2,end2])
            else:
                heapq.heappush(all_slots, [start1,end1])
        return []
        
    
        ## two pointer
        ## time O(nlogn), space O(n)
        slots1.sort()
        slots2.sort()
        point_1, point_2=0, 0
        while point_1<len(slots1) and point_2<len(slots2):
            start1, end1= slots1[point_1]
            start2, end2= slots2[point_2]
            if min(end2, end1)-max(start1,start2)>=duration:
                return [max(start1,start2), max(start1,start2)+duration]
            elif end1<=end2:
                point_1+=1
            else:
                point_2+=1
        return []