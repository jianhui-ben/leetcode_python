154. Find Minimum in Rotated Sorted Array II
class Solution:
    def findMin(self, nums: List[int]) -> int:
       # [4,5,6,7,0,1,4] 
        
        left, right = 0, len(nums)-1
        ## left boundary
        while left<=right:
            mid = left+(right-left)//2
            if mid-1>=0 and nums[mid]<nums[mid-1]:
                return nums[mid]
            elif nums[mid]>nums[right]:
                left=mid+1
            elif nums[mid]<nums[right]:
                right = mid-1
            else:
                right-=1
        return nums[left]
