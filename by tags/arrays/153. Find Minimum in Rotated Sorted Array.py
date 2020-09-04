#153. Find Minimum in Rotated Sorted Array

#Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

#(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

#Find the minimum element.

#You may assume no duplicate exists in the array.

#Example 1:

#Input: [3,4,5,1,2] 
#Output: 1
#Example 2:

#Input: [4,5,6,7,0,1,2]
#Output: 0


## binary search
def findMin(nums):
    mid= len(nums)//2
    out= nums[0]
    if len(nums)==1: return nums[0]
    elif len(nums)==2: return min(nums[1], nums[0])
    elif nums[0]< nums[mid]:
        return min(out, findMin(nums[mid:]))
    else: return min(out, findMin(nums[:mid+1]))

nums= [1,2,3] 
findMin(nums)