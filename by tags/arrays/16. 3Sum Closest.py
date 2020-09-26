#16. 3Sum Closest
#Given an array nums of n integers and an integer target, find three integers 
#in nums such that the sum is closest to target. Return the sum of the three integers.
#You may assume that each input would have exactly one solution.

 

#Example 1:

#Input: nums = [-1,2,1,-4], target = 1
#Output: 2
#Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

#Time O(n**2), space O(1)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) <3: return sum(nums)
        nums.sort()
        out=sum(nums[:3])
        min_dis= abs(out-target)
        for i in range(len(nums)-2):
            head, tail= i+1, len(nums)-1
            while head<tail:
                new_out= nums[i]+ nums[head]+nums[tail]
                if min(min_dis, abs(new_out-target))==abs(new_out-target):
                    min_dis= abs(new_out-target)
                    out= new_out
                if new_out<target:
                    head+=1
                elif new_out>target:
                    tail-=1
                else: return out
        return out
                
