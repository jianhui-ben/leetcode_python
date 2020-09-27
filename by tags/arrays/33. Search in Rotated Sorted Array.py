#33. Search in Rotated Sorted Array


#You are given an integer array nums sorted in ascending order, and an integer target.

#Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] 
#might become [4,5,6,7,0,1,2]).

#If target is found in the array return its index, otherwise, return -1.


#Example 1:

#Input: nums = [4,5,6,7,0,1,2], target = 0
#Output: 4
#Example 2:

#Input: nums = [4,5,6,7,0,1,2], target = 3
#Output: -1


##binary search with recursion
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursion(head, tail, target):
            if tail==head and nums[head]==target:
                return head
            elif tail-head<2:
                if nums[head]==target: return head
                elif nums[tail]==target: return tail
                else: return -1
            else:
                mid= (head+tail)//2
                if target== nums[mid]:
                    return mid
                elif nums[mid]>nums[head]:
                    if target>= nums[head] and target < nums[mid]:
                        return recursion(head,mid-1, target)
                    else: return recursion(mid+1, tail, target)
                elif nums[mid]< nums[head]:
                    if target>nums[mid] and target<= nums[tail]:
                        return recursion(mid+1, tail, target)
                    else: return recursion(head,mid-1, target)
        return recursion(0, len(nums)-1, target)





