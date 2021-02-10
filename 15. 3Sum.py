
#15. 3Sum
#Given an array nums of n integers, are there elements a, b, c in nums such 
#that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

#Notice that the solution set must not contain duplicate triplets.

 

#Example 1:

#Input: nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]
#Example 2:

#Input: nums = []
#Output: []
#Example 3:

#Input: nums = [0]
#Output: []


class Solution:
    
#     ## recursion: O(len(nums) !)
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         result=[]
#         nums.sort()
#         def recursion(cur_list, cur_sum,next_index):
#             if len(cur_list)==3 and cur_sum==0:
#                 if cur_list not in result:
#                     result.append(list(cur_list))  ## why this list is important

#             if len(cur_list)<3:
#                 for i in range(next_index, len(nums)):
#                     cur_list.append(nums[i])
#                     recursion(cur_list, cur_sum+nums[i], i+1)
#                     cur_list.pop()
            
#         recursion([], 0, 0)
#         return result

    ## iteration: for loop + two sum
    # time O(n**2); space O(1) or O(n) depends on the sorting algorithm
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3: return []
        result=[]
        nums.sort()
        for i in range(len(nums)-2):
            ##deal with replicates of the first value
            if i > 0 and nums[i]==nums[i-1]:
                continue
            
            head, tail= i+1,len(nums)-1
            target= 0- nums[i]
            while head<tail:
                if nums[head]+nums[tail]==target:
                    result.append(list([nums[i], nums[head], nums[tail]]))
                    head+=1
                    ##deal with the replicates of the second and third value
                    while nums[head]==nums[head-1] and head<tail:
                        head+=1
                elif nums[head]+nums[tail]<target:
                    head+=1
                else: tail-=1
        return result
