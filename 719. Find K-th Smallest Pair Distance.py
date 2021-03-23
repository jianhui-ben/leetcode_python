#719. Find K-th Smallest Pair Distance
#Given an integer array, return the k-th smallest distance among all the pairs. The distance of a pair (A, B) is defined as the absolute difference between A and B.

#Example 1:
#Input:
#nums = [1,3,1]
#k = 1
#Output: 0 
#Explanation:
#Here are all the pairs:
#(1,3) -> 2
#(1,1) -> 0
#(3,1) -> 2
#Then the 1st smallest distance pair is (1,1), and its distance is 0.

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        ## binary search to guess the number
        nums.sort()
        start, end = 0, nums[-1]-nums[0]
        
        def bi_search(nums, left, right, target):
            ## get the upper bound
            while left<=right:
                mid = left+(right-left)//2
                if nums[mid]<=target:
                    left=mid+1
                else:
                    right=mid-1
            if right<0 or nums[right]>target:
                return -1
            return right
        
        while start<=end:
            mid = start+ (end-start)//2
            count=0
            for i in range(len(nums)-1):
                result =  bi_search(nums, i+1, len(nums)-1, nums[i]+mid) ##right bound
                # print(i, result)
                if result!=-1:
                    count+=result-i
            if count<k:
                start=mid+1
            else:
                end = mid-1
        return start
                
                
                
                
                
            
         
        
        
        
        
        
        
        
        
        
        
#         ## Ben's method
#         ## pair distance increase from 0 to n, so we just keep counting how many pairs have distance of 0
#         ## 1, 2...n until the sum of pairs count reach k
        
#         #time O(k*n *logn)
#         target, start_dis,start_index=0, 0, 0
#         nums.sort()
#         # test= []
#         # print(nums)
#         def bi_search(arr, tar):
#             if tar<arr[0] or tar>arr[-1]: return -1
#             left, right = 0, len(arr)-1
#             while left<=right:
#                 mid = left+ (right-left)//2
#                 if arr[mid]==tar:
#                     right=mid-1
#                 elif arr[mid]>tar:
#                     right = mid-1
#                 else:
#                     left=mid+1
#             if left>=len(arr) or arr[left]!=tar:
#                 return -1
#             else: return left
        
        
#         while True:
#             while start_index<len(nums)-1:
#                 result_index=bi_search(nums[start_index+1:],nums[start_index]+start_dis)
#                 if result_index!=-1:
#                     target+=1
#                     # test.append((nums[start_index],nums[start_index+result_index+1]))
#                     while start_index+result_index+2<len(nums) and nums[start_index+result_index+1]==nums[start_index+result_index+2]:
#                         target+=1
#                         # test.append((nums[start_index],nums[start_index+result_index+1]))
#                         result_index+=1

#                 start_index+=1
#                 if target>=k:
#                     # print(test)
#                     return start_dis
#             start_dis+=1
#             start_index=0



