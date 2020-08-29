#Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

#Example 1:
#Input: [3, 2, 1]

#Output: 1

#Explanation: The third maximum is 1.
#Example 2:
#Input: [1, 2]

#Output: 2

#Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums))<3:
            return max(nums)
        return sorted(set(nums))[-3]