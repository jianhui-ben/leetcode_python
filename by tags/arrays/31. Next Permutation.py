#31. Next Permutation
#Implement next permutation, which rearranges numbers into the lexicographically
#next greater permutation of numbers.

#If such arrangement is not possible, it must rearrange it as the lowest possible order
#(ie, sorted in ascending order).

#The replacement must be in-place and use only constant extra memory.

#Here are some examples. Inputs are in the left-hand column and its corresponding outputs
#are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1: return
        
        replace= len(nums)-2
        while nums[replace]>= nums[replace+1] and replace>=0:
            replace-=1
        if replace==-1:
            nums.sort()
            return
        else:
            temp= len(nums)-1  ##temp=2; replace=0
            while nums[temp]<=nums[replace] and temp>replace:
                temp-=1
            # temp-=1
            # print(temp, replace)
            nums[temp], nums[replace]=nums[replace], nums[temp]
            for i in range((len(nums)-replace-1)//2):
                nums[i+ replace+1], nums[-(i+1)] =nums[-(i+1)], nums[i+ replace+1]
            return