#259. 3Sum Smaller
#Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

 

#Example 1:

#Input: nums = [-2,0,1,3], target = 2
#Output: 2
#Explanation: Because there are two triplets which sums are less than 2:
#[-2,0,1]
#[-2,0,3]
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        ## time O(N**2), space O(logn) -O(n) up to sorting method
        if len(nums) < 3: return 0
        
        nums.sort()
        out = 0
        
        for i in range(len(nums)-2):
            two_sum = target - nums[i]
            
            ##two pointer
            
            left, right = i + 1, len(nums)-1
            
            while left < right:
                
                if nums[left] + nums[right] < two_sum:
                    out +=  right - left
                    left += 1
                else:
                    right -= 1
        return out

        
        
        """
        sort it
        traverse nums and fix i:
        for i+1(j) and len(nums)-1(k):
            use two pointer:
            while j<k:
                if j+k < target - i:
                    out += k-j
                    j+= 1
                else:
                    k-=1
                    
        -2,0,1,3
        
        i =0
        
        
        nums[j] = 0
        nums[k] = 3
        target = 4
        
        out+= 2
        
        nums: []
        
        
        """