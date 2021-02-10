#210. Course Schedule II

#There are a total of n courses you have to take labelled from 0 to n - 1.

#Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] 
#this means you must take the course bi before the course ai.

#Given the total number of courses numCourses and a list of the prerequisite pairs, 
#return the ordering of courses you should take to finish all courses.

#If there are many valid answers, return any of them. If it is impossible to finish 
#all courses, return an empty array.

#Example 1:

#Input: numCourses = 2, prerequisites = [[1,0]]
#Output: [0,1]
#Explanation: There are a total of 2 courses to take. To take course 1 you should have 
#finished course 0. So the correct course order is [0,1].

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ## check the indegree of the node in graph:
        
        stored_prereq={i: 0 for i in range(numCourses)}
        stored_next_class= {b: set() for _,b in prerequisites}
        for a, b in prerequisites:
            stored_prereq[a]+=1
            stored_next_class[b].add(a)
        
        queue=[course for course, counts_prereq in stored_prereq.items() if counts_prereq==0]
        out=[]
        while queue:
            cur_course=queue.pop(0)
            out.append(cur_course)
            if cur_course in stored_next_class:
                for next_course in stored_next_class[cur_course]:
                    stored_prereq[next_course]-=1
                    if stored_prereq[next_course]==0:
                        queue.append(next_course)
        
        for _, counts in stored_prereq.items():
            if counts>0: return []
        return out
            

#         ##dfs:
#         stored_prereq={b: set() for b in range(numCourses)}
#         for a, b in prerequisites:
#             stored_prereq[a].add(b)
            
#         self.queue=[]
#         self.not_possible=False
        
#         def dfs(course, temp):
#             # print(temp)
#             if course in temp:
#                 self.not_possible=True
#                 return
#             if course not in self.queue:
#                 for next_c in stored_prereq[course]:
#                     dfs(next_c, temp+[course])
#                 self.queue.append(course)

#         for i in range(numCourses):
#             temp=[]
#             dfs(i, temp)
#             if self.not_possible: return []
#         return self.queue
