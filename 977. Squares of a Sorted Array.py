##977. Squares of a Sorted Array
#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

#Example 1:

#Input: nums = [-4,-1,0,3,10]
#Output: [0,1,9,16,100]
#Explanation: After squaring, the array becomes [16,1,0,9,100].
#After sorting, it becomes [0,1,9,16,100].
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ## two pointer
        left, right=0, len(nums)-1
        out=collections.deque()
        while left<=right:
            if abs(nums[left])>=abs(nums[right]):
                out.appendleft(nums[left]**2)
                left+=1
            else:
                out.appendleft(nums[right]**2)
                right-=1
        return out
        
                
            
            
        
