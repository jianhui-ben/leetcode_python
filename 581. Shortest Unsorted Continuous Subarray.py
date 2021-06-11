#581. Shortest Unsorted Continuous Subarray

#Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

#Return the shortest such subarray and output its length.

 

#Example 1:

#Input: nums = [2,6,4,8,10,9,15]
#Output: 5
#Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        ##stack O(n) O(n)
        
        stack = []
        left = len(nums)
        for i in range(len(nums)):
            if not stack or nums[i]>=nums[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums[i]<nums[stack[-1]]:
                    left = min(left, stack.pop())
                
        right = 0
        stack = []
        for i in range(len(nums)-1, -1, -1):
            if not stack or nums[i]<=nums[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums[i]>nums[stack[-1]]:
                    right = max(right, stack.pop())        
        
        if left>=right: return 0
        return right-left+1
                    

    
        # ## sorting O(nlogn) O(n)
        # sort_nums = sorted(nums)
        # left = 0
        # while left<len(nums):
        #     if nums[left]!=sort_nums[left]:
        #         break
        #     left+=1
        # if left==len(nums): return 0
        # right =len(nums)-1
        # while right>=0:
        #     if nums[right]!=sort_nums[right]:
        #         break
        #     right-=1
        # return right-left+1
        
        
      
        # O(n**2) solution 
        
#         left, right = len(nums)-1, 0
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[j]<nums[i]:
#                     left = min(left, i)
#                     right = max(right, j)
                    
#         if left>=right: return 0
        
#         return right-left+1
        
        