
#Given a sorted array nums, remove the duplicates in-place 
#such that each element appear only once and return the new length.

#Do not allocate extra space for another array, 
#you must do this by modifying the input array in-place with O(1) extra memory.

#Example 1:

#Given nums = [1,1,2],

#Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

#It doesn't matter what you leave beyond the returned length.

## wierd

def removeDuplicates(nums) -> int:
    len_ = 1
    if len(nums)==0:
        return 0
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[len_] = nums[i]
            len_ +=1
    return len_
