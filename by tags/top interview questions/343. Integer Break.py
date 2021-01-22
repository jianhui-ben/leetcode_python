#343. Integer Break

#Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

#Example 1:

#Input: 2
#Output: 1
#Explanation: 2 = 1 + 1, 1 × 1 = 1.

class Solution:
    def integerBreak(self, n: int) -> int:
        ##math: we optimize on *3 and *2
        if n==2: return 1
        elif n==3: return 2
        threes= n//3
        res= n%3
        
        if res==0:
            return 3**threes
        elif res==1:
            return 3**(threes-1)*4
        elif res==2:
            return 3**(threes)*2
