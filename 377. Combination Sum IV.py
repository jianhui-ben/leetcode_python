#377. Combination Sum IV
#Given an integer array with all positive numbers and no duplicates, 
#find the number of possible combinations that add up to a positive integer target.

#Example:

#nums = [1, 2, 3]
#target = 4

#The possible combination ways are:
#(1, 1, 1, 1)
#(1, 1, 2)
#(1, 2, 1)
#(1, 3)
#(2, 1, 1)
#(2, 2)
#(3, 1)

#Note that different sequences are counted as different combinations.

#Therefore the output is 7.
 

#Follow up:
#What if negative numbers are allowed in the given array?
#How does it change the problem?
#What limitation we need to add to the question to allow negative numbers?


##dp: time O(target* len(nums)), space: O(target)
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=[0 for _ in range(target)]
        nums.sort()
        cur_index=0
        for i in range(target):
            x= 0
            if i+1 in nums:
                x+=1
                cur_index= nums.index(i+1)
            for k in nums[: cur_index+1]:
                if i>=k:
                    x+=dp[i-k]
            dp[i]=x
        return dp[-1]

##follow-up
##if a negative number is allowed, then there'd be infinite number of combinations
## so we have to add a limitation to the problem saying each number in the nums list is only
## allowed to be used once.