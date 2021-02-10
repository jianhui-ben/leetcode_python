#78. Subsets
#Given an integer array nums, return all possible subsets (the power set).

#The solution set must not contain duplicate subsets.

 

#Example 1:

#Input: nums = [1,2,3]
#Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#Example 2:

#Input: nums = [0]
#Output: [[],[0]]

##time: O(n* 2**N); space: O(n* 2**N)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ##use binary mapping
        out=[]
        length= len(nums)
        for i in range(2**length, 2**(length+1)):
            mask= bin(i)[3:]
            
            out.append([nums[k] for k in range(length) if mask[k]=='1'])
        
        return out
        
#         ## every number could have 0/1 choose or not
#         out=[[]]
#         nums.sort()
        
#         for i in range(len(nums)):
#             temp=[]
#             if i!=0 and nums[i]==nums[i-1]:
#                 for cur_array in out:
#                     if nums[i] in cur_array:
#                         temp.append(cur_array+ [[nums[i]]])
#             else:
#                 for cur_array in out:
#                     temp.append(cur_array+[nums[i]])
#             out= out+ temp
#         return out
            