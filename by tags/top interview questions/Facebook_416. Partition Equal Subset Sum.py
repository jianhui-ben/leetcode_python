#416. Partition Equal Subset Sum

#Given a non-empty array nums containing only positive integers, 
#find if the array can be partitioned into two subsets such that 
#the sum of elements in both subsets is equal.

 

#Example 1:

#Input: nums = [1,5,11,5]
#Output: true
#Explanation: The array can be partitioned as [1, 5, 5] and [11].
#Example 2:

#Input: nums = [1,2,3,5]
#Output: false
#Explanation: The array cannot be partitioned into equal sum subsets.

class Solution:
    def partition(self, nums, index, cur_sums, target, memory):
        record= str(index)+ " "+ str(cur_sums)
        if record in memory:
            return memory[record]

        if cur_sums==target:
            bol=True
        elif cur_sums>target or index>= len(nums):
            bol= False
        else:
            bol= self.partition(nums, index+1, cur_sums, target, memory) or self.partition(nums, index+1, cur_sums+nums[index], target, memory)
        memory[record]=bol
        return bol
    
    
    
    def canPartition(self, nums: List[int]) -> bool:
        ## find a subarray which can sum to 1/2 of the total sum
        if sum(nums)%2!=0:
            return False
        if sum(nums)==0:
            return True
        nums.sort()
        target= sum(nums)/2
        return self.partition(nums, 0, 0, target, dict())