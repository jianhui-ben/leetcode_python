
#Given a non-empty array of integers, return the k most frequent elements.

#Example 1:

#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]
#Example 2:

#Input: nums = [1], k = 1
#Output: [1]
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        x= collections.Counter(nums).most_common(k)
        return [a for a, b in x]