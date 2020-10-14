
#Given an array, rotate the array to the right by k steps, where k is non-negative.

#Follow up:

#Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#Could you do it in-place with O(1) extra space?
 

#Example 1:

#Input: nums = [1,2,3,4,5,6,7], k = 3
#Output: [5,6,7,1,2,3,4]
#Explanation:
#rotate 1 steps to the right: [7,1,2,3,4,5,6]
#rotate 2 steps to the right: [6,7,1,2,3,4,5]
#rotate 3 steps to the right: [5,6,7,1,2,3,4]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        
#         ##method 1: brutal force time O(n*k); space O(1)        
#         for i in range(k):
#             prev= nums[-1]
#             for n in range(len(nums)-1, 0, -1):
#                 nums[n]=nums[n-1]
#             nums[0]=prev
        
        
        ## method 2: split into two array: space O(n), time  O(n)
        # copy= nums[:]
        # copy=copy[len(copy)-k:] + copy[: len(copy)-k]
        # for i in range(len(nums)):
        #     nums[i]= copy[i]            
        
        ## Method 3: one pass using cyclic replacement
        
#         n= start = 0
#         temp = None
#         while n< len(nums):
#             cur_index, temp= start, nums[start]
#             while True:
#                 next_index= (cur_index+ k)%len(nums)
#                 nums[next_index], temp= temp, nums[next_index]
#                 cur_index = next_index
#                 n+=1
#                 if start==cur_index: break
            
#             start+=1
            
        ## method 4: using reverse
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1
        n = len(nums)
        k %= n

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
        