#560. Subarray Sum Equals K

#Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

#Example 1:

#Input: nums = [1,1,1], k = 2
#Output: 2


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # ##brute force using cum_sum, time O(n**2), space O(n)
        # cum_sum=[0]
        # for i in nums:
        #     cum_sum.append(cum_sum[-1]+i)
        # out=0
        # for start in range(len(nums)):
        #     for end in range(start, len(nums)):
        #         if cum_sum[end+1]-cum_sum[start]==k:
        #             # print(end, start)
        #             out+=1
        # return out
        
        ##hashmap: very interesting method
        h, cum_sum, out={0:1}, 0, 0
        for i in nums:
            cum_sum+=i
            if cum_sum in h:
                h[cum_sum]+=1
            else:
                h[cum_sum]=1
            if (cum_sum- k) in h:
                if cum_sum-k== cum_sum:
                    out+=h[cum_sum- k]-1
                else:
                    out+=h[cum_sum- k]
        return out
            
        
        
        
