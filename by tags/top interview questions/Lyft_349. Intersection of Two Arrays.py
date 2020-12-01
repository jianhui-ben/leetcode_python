#349. Intersection of Two Arrays
#Given two arrays, write a function to compute their intersection.

#Example 1:

#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2]

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out=[]
        for i in set(nums1):
            if i in set(nums2):
                out.append(i)
        return out

        # set1 = set(nums1)
        # set2 = set(nums2)
        # return list(set2 & set1)
                
        