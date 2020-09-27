#18. 4Sum
#Given an array nums of n integers and an integer target, are there 
#elements a, b, c, and d in nums such that a + b + c + d = target? Find all 
#unique quadruplets in the array which gives the sum of target.

#Note:

#The solution set must not contain duplicate quadruplets.

#Example:

#Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

#A solution set is:
#[
#  [-1,  0, 0, 1],
#  [-2, -1, 1, 2],
#  [-2,  0, 0, 2]
#]

class Solution:

    ## for loop + three sum
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        nums.sort()
        for first in range(len(nums)-3):
            if first> 0 and nums[first]==nums[first-1]:
                continue
            elif nums[first]+nums[first+1]+ nums[first+2]+ nums[first+3]>target:
                break
            elif nums[first]+nums[len(nums)-1]+ nums[len(nums)-2]+ nums[len(nums)-3]<target:
                continue

            for second in range(first+1, len(nums)-2):
                if second> first+1 and nums[second]==nums[second-1]:
                    continue
                elif nums[first]+nums[second]+ nums[second+1]+ nums[second+2]>target:
                    break
                elif nums[first]+nums[second]+ nums[len(nums)-1]+ nums[len(nums)-2]<target:
                    continue
                head, tail = second +1, len(nums)-1
                while head<tail:
                    temp= nums[first]+nums[second]+ nums[head]+nums[tail]
                    if temp==target:
                        result.append(list([nums[first], nums[second], nums[head], nums[tail]]))

                        head+=1
                        ##deal with the replicates of the second and third value
                        while nums[head]==nums[head-1] and head<tail:
                            head+=1
                    elif temp<target: head+=1
                    elif temp > target: tail-=1
        return result