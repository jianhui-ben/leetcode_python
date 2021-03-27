#532. K-diff Pairs in an Array
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ## hashmap O(n), space O(n)
        hashmap = collections.Counter(nums)
        count=0
        for key, counts in hashmap.items():
            if k!=0:
                if key+k in hashmap:
                    count+=1
            else:
                if counts>1:
                    count+=1
        return count
                
        
        
        ## two pointer:
        ## time O(nlog n), space O(n) from sorting 
        if len(nums)==1: return 0
        nums.sort()
        left, right = 0, 1
        count=0
        while right<len(nums) and left<len(nums):
            if nums[right]-nums[left]==k:
                count+=1
                left+=1
                right+=1
            elif nums[right]-nums[left]>k:
                left+=1
            else:
                right+=1
            while left<len(nums) and nums[left]==nums[left-1]:
                left+=1
            while right<len(nums) and nums[right]==nums[right-1]:
                right+=1
            if left==right:
                right+=1
        return count
