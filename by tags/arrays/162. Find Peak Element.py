#162. Find Peak Element

#A peak element is an element that is greater than its neighbors.

#Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

#The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

#You may imagine that nums[-1] = nums[n] = -∞.

#Example 1:

#Input: nums = [1,2,3,1]
#Output: 2
#Explanation: 3 is a peak element and your function should return the index number 2.
#Example 2:

#Input: nums = [1,2,1,3,5,6,4]
#Output: 1 or 5 
#Explanation: Your function can return either index number 1 where the peak element is 2, 
#             or index number 5 where the peak element is 6.

##linear scan: time O(n) worst case; space O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==0: return None
        out= 0
        for i in range(1, len(nums)):
            if nums[i]>nums[i-1]:
                out= i
            else: return out
        return out

## recursive: time O(logn); space O(1)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def search(nums, start, end):
            if start==end:
                return start
            mid= (start+ end)//2
            if nums[mid]>nums[mid+1]:
                return search(nums, start, mid)
            else: return search(nums, mid+1, end)

        return search(nums, 0, len(nums)-1)


