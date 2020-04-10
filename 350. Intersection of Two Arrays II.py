#350. Intersection of Two Arrays II
#Given two arrays, write a function to compute their intersection.

#Example 1:

#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2,2]
#Example 2:

#Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#Output: [4,9]
#Note:

#Each element in the result should appear as many times as it shows in both arrays.
#The result can be in any order.

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans=[]
        while nums1:
            i= nums1.pop()
            if i in nums2:
                ans.append(i)
                nums2.remove(i)
        return ans
