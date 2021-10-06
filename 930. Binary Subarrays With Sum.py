#930. Binary Subarrays With Sum
#Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

#A subarray is a contiguous part of the array.

 

#Example 1:

#Input: nums = [1,0,1,0,1], goal = 2
#Output: 4
#Explanation: The 4 subarrays are bolded and underlined below:
#[1,0,1,0,1]
#[1,0,1,0,1]
#[1,0,1,0,1]
#[1,0,1,0,1]
#Example 2:

#Input: nums = [0,0,0,0,0], goal = 0
#Output: 15
 

#Constraints:

#1 <= nums.length <= 3 * 104
#nums[i] is either 0 or 1.
#0 <= goal <= nums.length

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        sliding window very smart 
        time O(n), space O(1)
        """
        def atMost(nums, goal):
            ans, cur_sum, left, right = 0, 0, 0, 0
            
            while right < len(nums):
                cur_sum += nums[right]
                right += 1

                while left < right and cur_sum > goal:
                    cur_sum -= nums[left]
                    left += 1
                ans += right - left
            return ans
        return atMost(nums, goal) - atMost(nums, goal - 1)

        
        
        
        
#         """
#         prefix sum for general cases:        
#         time O(N) space O(n)
#         """
#         pre_sum = [0]
#         for i in nums:
#             pre_sum.append(pre_sum[-1] + i)
#         count = defaultdict(int)
#         ans = 0
#         for i in pre_sum:
#             ans += count[i - goal]
#             count[i] += 1
            
#         return ans
        
        
        
#         """
#         brute force O(n**3)
#         """
#         out = 0
#         for i in range(len(nums)):
#             cur_sum = nums[i]
#             if cur_sum == goal:
#                 out += 1
            
#             for j in range(i + 1, len(nums)):
#                 cur_sum += nums[j]
#                 if cur_sum == goal:
#                     out += 1
                    
#         return out