#974. Subarray Sums Divisible by K
#Given an array nums of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by k.

 

#Example 1:

#Input: nums = [4,5,0,-2,-3,1], k = 5
#Output: 7
#Explanation: There are 7 subarrays with a sum divisible by k = 5:
#[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        ## stored the reminder so far into hashmap:
        stored=[0]*k
        stored[0]=1
        cur_sum, res= 0, 0
        for i in nums:
            cur_sum+=i
            res+=stored[cur_sum%k]
            stored[cur_sum%k]+=1
        return res

        
# [4,5,0,-2,-3,1] k = 5
# prefix sum:
# [4,9,9, 7, 4, 5 ]
#      i,
# res: 3, 
    



# 0: 1
# 1:
# 2:
# 3:
# 4:3 