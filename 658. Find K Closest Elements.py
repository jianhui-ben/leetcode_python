#658. Find K Closest Elements
#Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

#An integer a is closer to x than an integer b if:

#|a - x| < |b - x|, or
#|a - x| == |b - x| and a < b
 

#Example 1:

#Input: arr = [1,2,3,4,5], k = 4, x = 3
#Output: [1,2,3,4]

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         ##binary search to find the left boundary of window
#         if arr[0]>= x:
#             return arr[:k]
#         if arr[-1]<=x:
#             return arr[len(arr)-k::]
        
#         start, end = 0, len(arr)-k-1
#         while start<=end:
#             mid = start+(end-start)//2
#             ## we choose a window of k+1
#             if abs(arr[mid]-x)<=abs(arr[mid+k]-x):
#                 end= mid-1
#             else:
#                 start = mid+1
#         return arr[start:start+k]
            
        
        ## not correct. Need to rethink the sorting part
        if arr[0]>= x:
            return arr[:k]
        if arr[-1]<=x:
            return arr[len(arr)-k::]
        
        ## find the location of x in arr:
        left, right = 0, len(arr)-1
        while left<=right:
            mid = left+(right-left)//2
            if arr[mid]>=x:
                right = mid-1
            elif arr[mid]<x:
                left= mid+1
        if abs(arr[right]-x)>abs(arr[right+1]-x):
            right+=1
        # print(right)
        ## two pointer:
        start, end = max(right-k+1, 0), min(len(arr)-1, right+k-1)
        while end-start >k-1:
            if abs(arr[end]-x)>=abs(arr[start]-x):
                end-=1
            elif abs(arr[end]-x)<abs(arr[start]-x):
                start+=1
        return arr[start:end+1]
        