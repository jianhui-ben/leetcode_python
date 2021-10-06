#1838. Frequency of the Most Frequent Element

#The frequency of an element is the number of times it occurs in an array.

#You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

#Return the maximum possible frequency of an element after performing at most k operations.

 

#Example 1:

#Input: nums = [1,2,4], k = 5
#Output: 3
#Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
#4 has a frequency of 3.

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        sliding window
        max * size = cur_sum + k
        k = max * size - cur_sum
        """
        
        nums.sort()
        left, right, out, pre_sum = 0, 0, 0, 0
        
        while right < len(nums):
            
            pre_sum += nums[right]
            right += 1
            
            while nums[right - 1] * (right - left) - pre_sum > k:
                pre_sum -= nums[left]
                left += 1
            
            out = max(out, right - left)
        
        return out