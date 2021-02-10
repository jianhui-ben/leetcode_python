#523. Continuous Subarray Sum
#Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

 

#Example 1:

#Input: [23, 2, 4, 6, 7],  k=6
#Output: True
#Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ##brute force: time O(n3), space O(1)
        # for start in range(len(nums)-1):
        #     for end in range(start+1, len(nums)):
        #         tot= sum(nums[start:end+1])
        #         if tot==k or (k!=0 and tot%k==0):
        #             return True
        # return False
    
        # ## better brute force: O(n**2), space O(n)
        # cum_sum=[0]
        # temp=0
        # for i in nums:
        #     temp+=i
        #     cum_sum.append(temp)
        # for start in range(len(nums)-1):
        #     for end in range(start+1, len(nums)):
        #         tot= cum_sum[end+1]-cum_sum[start]
        #         if tot==k or (k!=0 and tot%k==0):
        #             return True
        # return False
        
        # hashmap + math
        if len(nums)<2: return False
        k=abs(k)
        #special case of 0
        if k==0:
            for i in range(len(nums)-1):
                if nums[i]==0 and nums[i+1]==0:
                    return True
            return False
        if k==1 and len(nums)>=2: return True
        mod_map=collections.defaultdict(None)
        mod_map[0]=-1
        cum_sum=0
        for i, v in enumerate(nums):
            cum_sum+=v
            # if cum_sum==k: return True
            if k!=0:
                mod=cum_sum%k
                # if mod==0: return True
                if mod not in mod_map:
                    mod_map[mod]=i
                elif i-mod_map[mod]>=2:
                    return True
        return False
