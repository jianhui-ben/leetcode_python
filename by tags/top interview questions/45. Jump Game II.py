#45. Jump Game II
#Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

#Each element in the array represents your maximum jump length at that position.

#Your goal is to reach the last index in the minimum number of jumps.

#You can assume that you can always reach the last index.

 

#Example 1:

#Input: nums = [2,3,1,1,4]
#Output: 2
#Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.


class Solution:
    def jump(self, nums: List[int]) -> int:
        
        ## greedy:
        n = len(nums)
        if n < 2:
            return 0 
        
        # max position one could reach 
        # starting from index <= i 
        max_pos = nums[0]
        # max number of steps one could do
        # inside this jump
        max_steps = nums[0]
        
        jumps = 1
        for i in range(1, n):
            # if to reach this point 
            # one needs one more jump
            if max_steps < i:
                jumps += 1
                max_steps = max_pos
            max_pos = max(max_pos, nums[i] + i)
                
        return jumps
        
        
        
        
#         ## bfs with mem
#         if not nums or len(nums)==1: return 0
#         queue=[0]
#         target=len(nums)
#         self.step=0
#         self.visited=set()
#         while queue:
#             self.step+=1
#             queue= self.bfs(queue, nums)
#         return self.step
    
#     def bfs(self, queue, nums):
#         target=len(nums)
#         temp=[]
#         for i in queue:
#             for step in range(nums[i], 0, -1):
#                 new_pos= i+step
#                 if new_pos in self.visited:
#                     continue
#                 if new_pos>=target-1:
#                     return []
#                 else:
#                     temp.append(new_pos)
#                     self.visited.add(new_pos)
#         return temp
            
        
        
