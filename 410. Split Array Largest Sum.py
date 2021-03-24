#410. Split Array Largest Sum
#Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.

#Write an algorithm to minimize the largest sum among these m subarrays.

 

#Example 1:

#Input: nums = [7,2,5,10,8], m = 2
#Output: 18
#Explanation:
#There are four ways to split nums into two subarrays.
#The best way is to split it into [7,2,5] and [10,8],
#where the largest sum among the two subarrays is only 18.


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        #O(N)
        ##use binary search to determine the largest sum
        ## for each guess, we run through the nums and see how many subarrays smaller or equal to the guess
        if m==1: return sum(nums)
        start, end = max(nums), sum(nums)
        while start<=end:
            mid = start+ (end-start)//2
            count, cum_sum=0, 0
            for i in range(len(nums)):
                cum_sum+=nums[i]
                if cum_sum>mid:
                    count+=1
                    if count>m:
                        break
                    cum_sum=nums[i]
            else:
                count+=1
                    
            #test
            # print(mid, count)
            
            if count>m:
                start=mid+1
            else:
                end = mid-1
        return start
        