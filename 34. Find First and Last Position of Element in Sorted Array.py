#34. Find First and Last Position of Element in Sorted Array

#Given an array of integers nums sorted in ascending order, find the starting and 
#ending position of a given target value.

#Your algorithm's runtime complexity must be in the order of O(log n).

#If the target is not found in the array, return [-1, -1].

#Example 1:

#Input: nums = [5,7,7,8,8,10], target = 8
#Output: [3,4]
#Example 2:

#Input: nums = [5,7,7,8,8,10], target = 6
#Output: [-1,-1]


def searchRange(nums, target):
    if len(nums)==0: return [-1, -1]
    def recursion_left(head, tail, target):
        if nums[head]==target: return head
        if tail-head<2 and target!= nums[head] and target!= nums[tail]: return -1
        mid= (head+tail)//2
        if nums[mid]==target and nums[mid-1]<target: return mid
        elif nums[mid]>=target:
            return recursion_left(head, mid-1, target)
        else: return recursion_left(mid+1, tail, target)   
    def recursion_right(head, tail, target):
        if nums[tail]==target: return tail
        if tail-head<2 and target!= nums[head] and target!= nums[tail]: return -1
        mid= (head+tail)//2
        if nums[mid]==target and nums[mid+1]>target: return mid
        elif nums[mid]>target:
            return recursion_right(head, mid-1, target)
        else: return recursion_right(mid+1, tail, target)
    return [recursion_left(0, len(nums)-1, target), recursion_right(0, len(nums)-1, target)]

nums = [5,7,7,8,8,10]
target = 8

searchRange(nums, target)
         

nums = [5,7,7,8,8,10]
def recursion_left(head, tail, target):
    if nums[head]==target: return head
    if tail-head<2 and target!= nums[head] and target!= nums[tail]: return -1
    mid= (head+tail)//2
    if nums[mid]==target and nums[mid-1]<target: return mid
    elif nums[mid]>target:
        return recursion_left(head, mid-1, target)
    else: return recursion_left(mid+1, tail, target)
recursion_left(0, len(nums)-1, target)

