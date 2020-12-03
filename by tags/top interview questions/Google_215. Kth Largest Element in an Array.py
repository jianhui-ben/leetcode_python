#215. Kth Largest Element in an Array

#Find the kth largest element in an unsorted array. Note that it is
#the kth largest element in the sorted order, not the kth distinct element.

#Example 1:

#Input: [3,2,1,5,6,4] and k = 2
#Output: 5


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]
##or we can use minHeap