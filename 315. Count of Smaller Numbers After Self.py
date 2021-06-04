#315. Count of Smaller Numbers After Self
#You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

 

#Example 1:

#Input: nums = [5,2,6,1]
#Output: [2,1,1,0]
#Explanation:
#To the right of 5 there are 2 smaller elements (2 and 1).
#To the right of 2 there is only 1 smaller element (1).
#To the right of 6 there is 1 smaller element (1).
#To the right of 1 there is 0 smaller element.


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
#         ## brute force is O(n**2)
        
#         out = [0]* len(nums)
#         for i in range(len(nums)-1, 0, -1):
#             for j in range(i, len(nums)):
#                 if nums[j]<nums[i-1]:
#                     out[i-1]+=1
#         return out
    
        ## n log n 
        import heapq
        out, checked=[None]* len(nums), []
        
        def binary_search(arr, target):
            if not arr: return -1
            low, high = 0, len(arr)-1
            while low<=high:
                mid=low+(high-low)//2
                if arr[mid]>=target:
                    high=mid-1
                elif arr[mid]<target:
                    low=mid+1
            return high

        
        for i in range(len(nums)-1, -1, -1):
            ## the last index where nums[j]<nums[i]
            index =  binary_search(checked, nums[i])
            checked.insert(index+1, nums[i])
            out[i] = index+1

            
        return out
            
        
        
        
        
        
        
        