#Given an array nums and a value val, remove all instances of that value in-place and return the new length.

#Do not allocate extra space for another array, you must do this by modifying 
#the input array in-place with O(1) extra memory.

#The order of elements can be changed. It doesn't matter what you leave beyond the new length.

#Example 1:

#Given nums = [3,2,2,3], val = 3,

#Your function should return length = 2, with the first two elements of nums being 2.

#It doesn't matter what you leave beyond the returned length.


## to make it in-place, I'd use switch
def removeElement(nums, val) -> int:
    head, count, tail= 0, 0, len(nums)-1
    while tail>=head:
        if nums[head]!=val:
            count+=1
            head+=1
        else:
            a, b=nums[head], nums[tail]
            nums[head], nums[tail]=b, a
            tail-=1
    return count


removeElement([0,1,2,2,3,0,4,2], 2)  ##5

