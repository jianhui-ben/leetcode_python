#905. Sort Array By Parity
#Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by all the odd elements of nums.

#You may return any answer array that satisfies this condition.

 

#Example 1:

#Input: nums = [3,1,2,4]
#Output: [2,4,3,1]
#The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        ## in place two pointer: O(n), O(1)
        left, right = 0, len(nums)-1
        while left < right:
            left_val, right_val = nums[left] % 2, nums[right] % 2
            if left_val == 0 and right_val == 0:
                left += 1
            elif left_val == 1 and right_val == 1:
                right -= 1
            elif left_val == 1 and right_val == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            else:
                left += 1
                right -= 1
        return nums
              
        
#         ## two pointer O(n), O(n)
#         if not nums: return []
#         output = [None] * len(nums)
#         left, right, cur_i = 0, len(nums)-1, 0
        
#         while left <= right:
#             if nums[cur_i] % 2 == 0:
#                 output[left] = nums[cur_i]
#                 left += 1
#             else:
#                 output[right] = nums[cur_i]
#                 right -= 1
#             cur_i += 1
            
#         return output
