##621. Task Scheduler

#Given a characters array tasks, representing the tasks a CPU needs to do,
#where each letter represents a different task. Tasks could be done in any order. 
#Each task is done in one unit of time. For each unit of time, the CPU could 
#complete either one task or just be idle.

#However, there is a non-negative integer n that represents the cooldown period 
#between two same tasks (the same letter in the array), that is that there must 
#be at least n units of time between any two same tasks.

#Return the least number of units of times that the CPU will take to finish all the given tasks.

 

#Example 1:

#Input: tasks = ["A","A","A","B","B","B"], n = 2
#Output: 8
#Explanation: 
#A -> B -> idle -> A -> B -> idle -> A -> B
#There is at least 2 units of time between any two same tasks.






class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ##greedy search using priority quue
        import collections
        
        out, heap= 0, []
        tasks_coll= collections.Counter(tasks)
        for key, counts in tasks_coll.items():
            heapq.heappush(heap, (-counts, key))
        
        while heap:
            temp, i=[], 0
            for i in range(n+1):
                out+=1
                if heap:
                    counts, key= heapq.heappop(heap)
                    counts+=1
                    if counts<0:
                        temp.append((counts, key))
                if not heap and not temp: break
                    
            for counts, key in temp:
                heapq.heappush(heap, (counts, key))
        return out
                    
        