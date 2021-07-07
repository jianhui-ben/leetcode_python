#360. Sort Transformed Array
#Given a sorted integer array nums and three integers a, b and c, apply a quadratic function of the form f(x) = ax2 + bx + c to each element nums[i] in the array, and return the array in a sorted order.

 

#Example 1:

#Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
#Output: [3,9,15,33]
from collections import deque
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        """
        [-4,-2,2,4], a = 1, b = 3, c = 5
        
        bx + c
        
        [-7, -1, 11, 17]
          
        ax**2
        
        
        
        [16, 4, 4, 16]
        [9, 3, 15, 33]
        
        
        
        
        
        [-4,-2,2,4], a = -1, b = 3, c = 5
        bx + c
        [-7, -1, 11, 17]
        ax**2
        [-16, -4, -4, -16]
        
        [-23, -5, 1, 7]
        """
        q = deque([])
        left, right = 0, len(nums) - 1
        
        if a < 0:
            while left <= right:
                left_num, right_num = a * (nums[left])**2 + b * (nums[left]) + c,\
                                      a * (nums[right])**2 + b * (nums[right]) + c
                
                if left_num <= right_num:
                    q.append(left_num)
                    left += 1
                else:
                    q.append(right_num)
                    right -= 1
        elif a > 0 :
            while left <= right:
                left_num, right_num = a * (nums[left])**2 + b * (nums[left]) + c,\
                                      a * (nums[right])**2 + b * (nums[right]) + c
                
                if left_num >= right_num:
                    q.appendleft(left_num)
                    left += 1
                else:
                    q.appendleft(right_num)
                    right -= 1 
        elif b < 0: return reversed([b * i + c for i in nums])
        elif b >= 0: return [b * i + c for i in nums]
        return q
                    
                
            
        
        
        
        
        
        
        
        