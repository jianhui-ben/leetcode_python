#Given a sorted array and a target value, return the index if 
#the target is found. If not, return the index where it would be if it were inserted in order.

#You may assume no duplicates in the array.

#Example 1:

#Input: [1,3,5,6], 5
#Output: 2

def searchInsert(nums, target) -> int:
    i=0
    while i<len(nums):
        if nums[i]>=target:
            return i
        i+=1
    return len(nums)
    

searchInsert([1,3,5,6], 7)  ##4