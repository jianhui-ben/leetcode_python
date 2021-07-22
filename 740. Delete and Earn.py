#740. Delete and Earn
#You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

#Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
#Return the maximum number of points you can earn by applying the above operation some number of times.

 

#Example 1:

#Input: nums = [3,4,2]
#Output: 6
#Explanation: You can perform the following operations:
#- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
#- Delete 2 to earn 2 points. nums = [].
#You earn a total of 6 points.
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        dp with constant space
        """
        counter = collections.Counter(nums)
        
        prev = None
        using, not_using = 0, 0
        for i in sorted(counter):
            if i - 1 != prev:
                using, not_using = i * counter[i] + max(using, not_using), \
                                  max(using, not_using)
            else:
                using, not_using = i * counter[i] + not_using, \
                                  max(using, not_using)
            prev = i
        return max(using, not_using)
        