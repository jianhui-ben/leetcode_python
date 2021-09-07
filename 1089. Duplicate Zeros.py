#1089. Duplicate Zeros
#Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

#Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

#Example 1:

#Input: arr = [1,0,2,3,0,4,5,0]
#Output: [1,0,0,2,3,0,0,4]
#Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        O(n), O(n)
        """      
#         copy = arr[:]
#         a_i, c_i = 0, 0
        
#         while a_i < len(arr):
#             arr[a_i] = copy[c_i]
#             if not copy[c_i]:
#                 a_i += 1
#                 if a_i < len(arr):
#                     arr[a_i] = 0
#             a_i += 1
#             c_i += 1
        """
        2nd approach: O(n), O(1) space
        """
        
        original_i, expanded_i = len(arr) - 1, len(arr) + arr.count(0) - 1
        
        while expanded_i >= 0 :
            
            if expanded_i < len(arr):
                arr[expanded_i] = arr[original_i]
            expanded_i -= 1
            if arr[original_i] == 0:
                if expanded_i < len(arr):
                    arr[expanded_i] = arr[original_i]
                expanded_i -= 1
            original_i -= 1
            