#633. Sum of Square Numbers
#Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

#Example 1:

#Input: c = 5
#Output: true
#Explanation: 1 * 1 + 2 * 2 = 5


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        """
        binary search
        """
        def bst(left, right, target):
            while left <= right:
                mid = left + (right - left) // 2
                mid_sq = mid * mid
                if mid_sq == target:
                    return mid
                elif mid_sq > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        for a in range(int(c ** 0.5) + 1):
            if bst(0, c - a**2, c - a**2) >= 0 :
                return True
            
        return False
            