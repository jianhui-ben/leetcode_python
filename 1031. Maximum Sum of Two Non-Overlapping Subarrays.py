#1031. Maximum Sum of Two Non-Overlapping Subarrays
#Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.

#The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.

#A subarray is a contiguous part of an array.

 

#Example 1:

#Input: nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2
#Output: 20
#Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        """
        O(n) time space can be compressed
        """
        prefix_sum = [0]
        
        for i in nums:
            prefix_sum.append(i + prefix_sum[-1])
        
        res, first_max, sec_max = 0, 0, 0
        
        """
        [1,0,3], 1, 2
        0, 1, 1, 4
              ^
        """
        
        ## first before second
        for i in range(firstLen, len(prefix_sum) - secondLen):
            sec_sum = prefix_sum[i + secondLen] - prefix_sum[i]
            first_max = max(first_max, prefix_sum[i] - prefix_sum[i - firstLen])
            res = max(res, sec_sum + first_max)
            
        for i in range(secondLen, len(prefix_sum) - firstLen):
            fir_sum = prefix_sum[i + firstLen] - prefix_sum[i]
            sec_max = max(sec_max, prefix_sum[i] - prefix_sum[i - secondLen])
            res = max(res, fir_sum + sec_max)          
            
        return res
        