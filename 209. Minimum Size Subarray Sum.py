#209. Minimum Size Subarray Sum


#Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous 
#subarray of which the sum ≥ s. If there isn't one, return 0 instead.

#Example: 

#Input: s = 7, nums = [2,3,1,2,4,3]
#Output: 2
#Explanation: the subarray [4,3] has the minimal length under the problem constraint.
#Follow up:
#If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ## brute force: time O(n**2); space: O(1)
        if sum(nums)<s: return 0
        ans= len(nums)
        for i in range(len(nums)):
            total=0
            count= 0
            for k in range(i, len(nums)):
                total+= nums[k]
                count+=1
                if total>= s:
                    ans=min(ans, count)
                    break
        return ans
            


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:       
        ## better brute force using memorization
        if sum(nums)<s: return 0
        sum_arr= [0]* (len(nums)+1)
        for i in range(len(nums)):
            sum_arr[i+1]= sum_arr[i]+nums[i]
        sum_arr.pop(0)    
        start, end, ans= 0, len(nums)-1, len(nums)
        for start in range(len(nums)):
            for end in range(start, len(nums)):
                if sum_arr[end]-sum_arr[start]+nums[start]>=s:
                    ans=min(ans, end-start+1)
        return ans


## two pointer: time O(n), space O(1)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        head, tail, total= 0,0, 0
        result= float('inf')
        for i in range(len(nums)):
            total+= nums[i]
            tail+=1
            while total>=s:
                result= min(result,  tail- head)
                total-= nums[head]
                head+=1
        if result==float('inf'): return 0
        else: return result
                