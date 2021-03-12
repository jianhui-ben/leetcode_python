#90. Subsets II
#Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

#The solution set must not contain duplicate subsets. Return the solution in any order.

 

#Example 1:

#Input: nums = [1,2,2]
#Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        def dfs(nums, idx, cur):
            nonlocal out
            out.append(cur)
            if idx ==len(nums):
                return
            for i in range(idx, len(nums)):
                if i>idx and nums[i]==nums[i-1]:
                    continue
                dfs(nums, i+1, cur+[nums[i]])
        
        dfs(nums, 0, [])
        return out
