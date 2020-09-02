
#167. Two Sum II - Input array is sorted

#Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific 
#target number.

#The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be 
#less than index2.

#Note:

#Your returned answers (both index1 and index2) are not zero-based.
#You may assume that each input would have exactly one solution and you may not use the same element twice.
#Example:

#Input: numbers = [2,7,11,15], target = 9
#Output: [1,2]
#Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.


class Solution:
    
    ### use two pointers
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head, tail= 0, len(numbers)-1
        while head< tail:
            if numbers[head]+numbers[tail]==target:
                return [head+1, tail+1]
            elif numbers[head]+numbers[tail]>target:
                tail-=1
            else: head+=1
        return [head+1, tail+1]