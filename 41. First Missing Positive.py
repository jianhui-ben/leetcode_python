#Given an unsorted integer array nums, find the smallest missing positive integer.

#You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

#Example 1:

#Input: nums = [1,2,0]
#Output: 3
#Example 2:

#Input: nums = [3,4,-1,1]
#Output: 2
#Example 3:

#Input: nums = [7,8,9,11,12]
#Output: 1


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ## index sorting: this is not typical sorting the array
        ## O(n), O(1)
        ##[1,1, 2,2, 4, 11]
        ## remove 0 or -1 or some too large numbers
        if 1 not in nums: return 1
        
        for i in range(len(nums)):
            if nums[i]<=0 or nums[i]> len(nums):
                nums[i] =1
        #[0, 1,1, 2,2, 4, 1]
        nums = [0] + nums
        
        print(nums)
        ## [0, 1,2,1, 4, 2, 1]
        
        ## [0, 1,2]
        ## 
        temp_cnt = 1
        for i in range(1, len(nums)):
            while nums[i]!= i and nums[i]>0 and nums[i]<len(nums) and nums[nums[i]]!= nums[i]:
                nums[nums[i]], nums[i]= nums[i], nums[nums[i]]
                # temp = nums[nums[i]]
                # nums[nums[i]] = nums[nums[i]]
                # nums[i] = temp
                
        for i in range(len(nums)):
            if nums[i]!=i: return i
            
        
        ## in case it's [1,2,3,4]
        return len(nums)
        

        
        
        ## using heap O(n log n), O(1) since heap is in-place
        
#         import heapq
#         heapq.heapify(nums)
#         target = 1
#         for _ in range(len(nums)):
#             low = heapq.heappop(nums)
#             if low == target:
#                 target+=1
#         return target
