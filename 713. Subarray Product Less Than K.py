#713. Subarray Product Less Than K
#Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

#Example 1:

#Input: nums = [10,5,2,6], k = 100
#Output: 8
#Explanation: The 8 subarrays that have product less than 100 are:
#[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
#Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        """
        sliding window
        """
        left, right = 0, 0
        window_product = 1
        out = 0
        while right < len(nums):
            
            if nums[right] < k:
                window_product *= nums[right]
                right += 1
                
                while window_product >= k:
                    window_product /= nums[left]
                    left += 1
                
                out += right - left

                
            else:
                left, right = right + 1, right + 1
                window_product = 1
        return out
                