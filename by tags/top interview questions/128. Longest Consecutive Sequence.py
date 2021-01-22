#128. Longest Consecutive Sequence
#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

#Follow up: Could you implement the O(n) solution? 

 

#Example 1:

#Input: nums = [100,4,200,1,3,2]
#Output: 4
#Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        ## brute force
        nums.sort()
        if not nums: return 0
        out, cur= 1, 1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]== nums[i-1]+1:
                cur+=1
            else:
                out= max(out, cur)
                cur= 1
        return max(out, cur)
        