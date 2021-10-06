#870. Advantage Shuffle
#You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

#Return any permutation of nums1 that maximizes its advantage with respect to nums2.

 

#Example 1:

#Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
#Output: [2,11,7,15]

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        """
        sort both array
        two pointers
        time: nlogn, space: n
        """
        s1, s2 = sorted(nums1, reverse = True), sorted(nums2, reverse = True)
        
        out = []
        
        left, right = 0, len(s1) - 1
        for i in range(len(s2)):
            if s1[left] > s2[i]:
                out.append(s1[left])
                left += 1
            else:
                out.append(s1[right])
                right -= 1
        
        match = defaultdict(list)
        for i in range(len(out)):
            match[s2[i]].append(out[i])
        
        out = []
                
        for num2 in nums2:
            out.append(match[num2].pop())
        
        return out
                