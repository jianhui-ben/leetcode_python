#207. Course Schedule
#There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

#For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
#Return true if you can finish all courses. Otherwise, return false.

 

#Example 1:

#Input: numCourses = 2, prerequisites = [[1,0]]
#Output: true
#Explanation: There are a total of 2 courses to take. 
#To take course 1 you should have finished course 0. So it is possible.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## post order dfs:
        stored_prep=collections.defaultdict(set)
        for a, b in prerequisites:
            stored_prep[a].add(b)
        
        self.check=set()
        def dfs(i, visited):
            nonlocal stored_prep
            if i in visited:
                return False
            for prep in stored_prep[i]:
                if prep not in self.check:
                    res= dfs(prep, visited+[i])
                    if not res: return False
                    else:
                        self.check.add(prep)
            return True

        
        for i in range(numCourses):
            if i in self.check:
                continue
            if not dfs(i, []): return False
            self.check.add(i)
        return True

#         ##Ben's method
#         stored_prep=collections.defaultdict(set)
#         for a, b in prerequisites:
#             stored_prep[a].add(b)
        
#         def dfs(cur_i, temp):
#             nonlocal stored_prep
#             if cur_i in temp:
#                 return False
#             for pre_i in stored_prep[cur_i]:
#                 if pre_i in self.visited:
#                     continue
#                 if not dfs(pre_i, temp+ [cur_i]):
#                     return False
#             return True
        
#         self.visited=set()
#         for i in range(numCourses):
#             if not dfs(i, []): 
#                 return False
#             self.visited.add(i)
#         return True
