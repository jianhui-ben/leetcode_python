
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
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ##here is binary search: O(nlogn)
#         def bi_search(arr, target):
#             left, right =0, len(arr)-1
#             while left<=right:
#                 mid = left+(right-left)//2
#                 if arr[mid]==target:
#                     return mid
#                 elif arr[mid]>target:
#                     right = mid-1
#                 else:
#                     left=mid+1
#             return None
#         for i in range(len(numbers)):
#             if target-numbers[i]<= numbers[-1]:
#                 sec=bi_search(numbers[i+1:], target-numbers[i])
#                 if sec is not None: return sorted([i+1, i+sec+2])
                
        ##better use two pointers
        ##O(n)
        left, right =0, len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]==target:
                return [left+1, right+1]
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1